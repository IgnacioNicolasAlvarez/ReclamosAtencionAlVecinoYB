import scrapy


class ReclamosybItem(scrapy.Item):
    title = scrapy.Field()
    resource_name = scrapy.Field()
    resource_link = scrapy.Field()
