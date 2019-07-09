# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class BossScrapyPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        walden = client['Boss']
        self.sheet_tab = walden['details2']

    def process_item(self, item, spider):
        self.sheet_tab.insert_one(item)
        return item

class ProxyPoolPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        proxie_url = client['proxies']
        self.sheet_tab = proxie_url['sheet_tab']

    def process_item(self, item, spider):
        self.sheet_tab.insert_one(item)
        return item