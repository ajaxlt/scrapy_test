# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:

    _id = scrapy.Field()
    name = scrapy.Field()
    recuit_num = scrapy.Field()
    req_education = scrapy.Field()
    dep_name = scrapy.Field()

    pass
