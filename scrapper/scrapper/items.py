from scrapy.item import Item, Field


class BreweryItem(Item):
    name = Field()
    location = Field()
    # Type of brewery.
    type = Field()


