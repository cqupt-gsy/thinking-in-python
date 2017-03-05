# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MissingChildItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    sex = scrapy.Field()
    birth_date = scrapy.Field()
    missing_date = scrapy.Field()
    province = scrapy.Field()
    missing_place = scrapy.Field()
    police_call = scrapy.Field()
    dna = scrapy.Field()
    url = scrapy.Field()
    pass
