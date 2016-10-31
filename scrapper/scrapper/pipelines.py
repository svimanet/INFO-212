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
        d = self.dbpool.runInteraction(self._do_upsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    def _do_upsert(self, conn, item, spider):
        """Perform an insert or update."""
        #print(item)
        #print(item["address"])
        conn.execute("""
            INSERT INTO breweries
                (name,address,type)
            VALUES (%s,%s,%s)
        """, (item['name'],item['address'],item['type']))
        self.stats.inc_value("database/insert")
        spider.log("Item stored in db: %s %r" % (id, item))
        return item

    def _handle_error(self, failure, item, spider):
        """Handle occurred on db interaction."""
        # do nothing, just log
        log.err(failure)

