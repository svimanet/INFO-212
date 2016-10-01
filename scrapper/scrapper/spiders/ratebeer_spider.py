
from scrapy.spiders import CrawlSpider, Rule
from scrapper.items import BreweryItem

from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.linkextractors import LinkExtractor as sle

from scrapy.exceptions import DropItem



class ArticleScapper(CrawlSpider):
    name = "ratebeer"
    allowed_domains = ["ratebeer.com"]
    start_urls = [
        	"http://www.ratebeer.com/breweries/norway/0/154/"
                  ]
    rules = [
        Rule(sle(
            allow=("/brewers/*"),
        ), callback='parse_1')]

    def parse_1(self, response):
        self.response = response
        self.selector = Selector(response)
        item = BreweryItem()

 	print(self.selector.xpath('//h1[@itemprop="name"]/text()').extract()[0])

        return item
