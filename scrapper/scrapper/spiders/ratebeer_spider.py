
from scrapy.spiders import CrawlSpider, Rule
from scrapper.items import ArticleItem

from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor as sle

from scrapy.exceptions import DropItem



class ArticleScapper(CrawlSpider):
    name = "ratebeer"
    allowed_domains = ["ratebeer.com"]
    start_urls = [
                  ]
    rules = [
        Rule(sle(
            allow=("/nyheter/.*"),
        ), callback='parse_1')]

    def parse_1(self, response):
        self.response = response
        self.selector = Selector(response)
        item = ArticleItem()

        item["title"] = self.selector.xpath('//head//meta[@property="og:title"]//@content').extract()[0]
        item["entity"] = "ap"
        item["article"] = "".join(self.selector.xpath('//div[contains(@class, "widget storyContent bodyText")]').extract()).encode("utf-8")
        item["url"] = self.response.url

        return item
