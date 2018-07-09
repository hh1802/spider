# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItem(scrapy.Item):
    collection = 'shuju'
    number = scrapy.Field()
    red_ball = scrapy.Field()
    blue_ball = scrapy.Field()



