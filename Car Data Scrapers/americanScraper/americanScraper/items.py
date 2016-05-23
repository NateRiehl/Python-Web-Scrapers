import scrapy
class AmericanscraperItem(scrapy.Item):
	Type = scrapy.Field()
	Vendor = scrapy.Field()
	Title = scrapy.Field()
	Option3_Name = scrapy.Field()
	Option2_Name = scrapy.Field()
	Option1_Name = scrapy.Field()
	Option3_Value = scrapy.Field()
	Option2_Value = scrapy.Field()
	Option1_Value = scrapy.Field()
