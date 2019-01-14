# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdprojectItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    pass


class ProductTypeItem(scrapy.Item):
    id = scrapy.Field()
    pid = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    pass


class ProductItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    brandId = scrapy.Field()
    shopId = scrapy.Field()
    imgUrl = scrapy.Field()
    price = scrapy.Field()
    detailPage = scrapy.Field()



