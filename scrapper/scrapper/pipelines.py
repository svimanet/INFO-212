# -*- coding: utf-8 -*-
from scrapy import signals
import sys
from scrapy import log

from scrapy.item import BaseItem
from scrapy.exceptions import DropItem

from twisted.enterprise import adbapi


class MySQLStorePipeline(object):

    def __init__(self, dbpool, table, stats):
        self.dbpool = dbpool
        self.table = table
        self.stats = stats


    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        crawler.stats.set_value('database/insert', 0)
        crawler.stats.set_value('database/update', 0)
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool, settings['MYSQL_TABLE'], crawler.stats)

    def process_item(self, item, spider):
        # run db query in the thread pool
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        # at the end return the item in case of success or failure
        d.addBoth(lambda _: item)
        # return the deferred instead the item. This makes the engine to
        # process next item (according to CONCURRENT_ITEMS setting) after this
        # operation (deferred) has finished.
        return d

    def _do_upsert(self, conn, item, spider):
        """Perform an insert or update."""

        conn.execute("SELECT updatedDate FROM articles WHERE _id=%s", (item["id"], ))
        ret = conn.fetchone()

        if ret:
            conn.execute("""
                UPDATE articles
                SET title=%s, article=%s, updatedDate=%s, ingress=%s, pubDate=%s
                WHERE _id=%s
            """, (item["title"], item['article'], item['updatedDate'], item['ingress'], item["pubDate"], item["id"]))
            self.stats.inc_value("database/update")
            spider.log("Item updated in db: %s %r" % (item["id"], item))
        else:
            conn.execute("""
                INSERT INTO articles
                    (_id, title, ingress, article, imgThumb, imgLarge, category, source, sourceUrl, updatedDate, pubDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (item["id"], item['title'], item['ingress'], item['article'], item['imgThumb'], item['imgLarge'],
                  item['category'], item['source'], item['sourceUrl'], item['updatedDate'], item['pubDate']))
            self.stats.inc_value("database/insert")
            spider.log("Item stored in db: %s %r" % (id, item))
        return item

    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

