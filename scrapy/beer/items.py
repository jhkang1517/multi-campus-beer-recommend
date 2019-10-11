# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BeerItem(scrapy.Item):
    name = scrapy.Field()
    style = scrapy.Field()
    country = scrapy.Field()
    company = scrapy.Field()
    avg = scrapy.Field()
    alcohol = scrapy.Field()
    available = scrapy.Field()
    review_ct = scrapy.Field()
    score = scrapy.Field()
    review = scrapy.Field()

# class BeerItem2(scrapy.Item):
#     name = scrapy.Field()
#     country = scrapy.Field()
#     avg = scrapy.Field()
#     alcohol = scrapy.Field()
#     available = scrapy.Field()
#     reviews_count = scrapy.Field()