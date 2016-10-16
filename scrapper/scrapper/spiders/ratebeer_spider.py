
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

        name = self.selector.xpath('//h1[@itemprop="name"]/text()').extract()
        if name:
            item["name"] = name[0]

        address = self.selector.xpath('//span[@itemprop="streetAddress"]/text()').extract()
        if address:
            item["address"] = address[0]

        locality = self.selector.xpath('//span[@itemprop="addressLocality"]/text()').extract()
        if locality:
            item["locality"] = locality[0]

        country = self.selector.xpath('//span[@itemprop="addressCountry"]/text()').extract()
        if country:
            item["country"] = country[0]

        postal_code = self.selector.xpath('//span[@itemprop="postalCode"]/text()').extract()
        if postal_code:
            item["postal_code"] = postal_code[0]

        type = self.selector.xpath("(//div[@itemtype='http://schema.org/LocalBusiness']//div/text()[2]").extract()
        print(type)
        if type:
            item["type"] = type[0].strip()

        return item
