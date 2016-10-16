from scrapy.item import Item, Field


class BreweryItem(Item):
    name = Field()
    address = Field()
    locality = Field()
    country = Field()
    postal_code = Field()
    # Type of brewery.
    type = Field()


