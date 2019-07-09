# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossIndexScrapyItem(scrapy.Item):
    url = scrapy.Field()
    classify = scrapy.Field()
    type = scrapy.Field()
    nationwide_url = scrapy.Field()


class BossScrapyItem(scrapy.Item):
    l_title = scrapy.Field()
    l_salary = scrapy.Field()
    l_experience = scrapy.Field()
    l_company = scrapy.Field()
    l_url = scrapy.Field()
    l_education = scrapy.Field()
    l_location = scrapy.Field()
    l_type = scrapy.Field()



