# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QcwyItem(scrapy.Item):

    job_name = scrapy.Field()
    company = scrapy.Field()
    area = scrapy.Field()
    salary = scrapy.Field()
    pabulish_time = scrapy.Field()

