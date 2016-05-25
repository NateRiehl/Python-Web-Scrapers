# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KmcItem(scrapy.Item):
	Type = scrapy.Field()
	Vendor = scrapy.Field()
	Title = scrapy.Field()
	Option1Name = scrapy.Field()
	MultipleOptionValues1 = scrapy.Field()	
	Option2Name = scrapy.Field()
	MultipleOptionValues2 = scrapy.Field()
	Option3Name = scrapy.Field()
	MultipleOptionValues3 = scrapy.Field()
	ImageSrc = scrapy.Field()
