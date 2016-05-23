# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MotometalscraperItem(scrapy.Item):
	Type = scrapy.Field()
	Vendor = scrapy.Field()
	Title = scrapy.Field()
	Option3_Name = scrapy.Field()
	Option2_Name = scrapy.Field()
	Option1_Name = scrapy.Field()
	Option3_Value = scrapy.Field()
	Option2_Value = scrapy.Field()
	Option1_Value = scrapy.Field()