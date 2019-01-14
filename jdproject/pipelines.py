# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jdproject.items import ProductTypeItem
from jdproject.items import JdprojectItem
from jdproject.items import ProductItem
import pymongo


class JdprojectPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        db = client['jd']
        self.post = db['category']

    def process_item(self, item, spider):
        if isinstance(item, ProductTypeItem):
            postItem = dict(item)
            self.post.insert(postItem)
            print("jdpt")
        elif isinstance(item, JdprojectItem):
            print("jdimage")
        elif isinstance(item, ProductItem):
            print("ProductItem")
        else:
            print("other")
        return item


class JdProductPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        db = client['jd']
        self.post = db['product']

    def process_item(self, item, spider):
        if isinstance(item, ProductItem):
            postItem = dict(item)
            self.post.insert(postItem)
            print('product')
        return item
