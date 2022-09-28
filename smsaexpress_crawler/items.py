# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SmsaexpressItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tracking_number = scrapy.Field()
    final_status = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    status = scrapy.Field()
    location = scrapy.Field()
