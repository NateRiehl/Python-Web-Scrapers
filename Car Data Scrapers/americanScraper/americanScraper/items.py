import scrapy
class AmericanscraperItem(scrapy.Item):
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
	url = scrapy.Field()

	
