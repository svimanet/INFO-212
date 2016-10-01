from scrapy.item import Item, Field


class ArticleItem(Item):
    title = Field()
    article = Field()
    url = Field()
    entity = Field()


