import scrapy
import urlparse
from americanScraper.items import AmericanscraperItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import FormRequest

class AmericanSpider(scrapy.Spider):
	name = 'american'
	allowed_domains = ['americanforcewheels.com']
	start_urls = [
		'http://americanforcewheels.com/'
	]
	
	def parse(self,response):
		base_url = get_base_url(response)
		print(response)
# 		for sel in response.xpath('//div[@id="WheelsGallery1"]/a'):
# 			item = AmericanscraperItem()
# 			item['Type'] = 'Rims'
# 			item['Vendor'] = 'American Force'
# 			item['Option3_Name'] = 'Wheels'
# 			item['Option3_Value'] = '2,4,5,6'
# 			item['Title'] = sel.xpath('div/p/text()').extract()
# 			title = sel.xpath('').extract()
# 			item['Option2_Name'] = 'Color'
# 			item['Option2_Value'] = title[0]
# 			relative_url = sel.xpath('').extract()
#  			url = [urljoin_rfc(base_url,ru) for ru in relative_url]
# 			request = scrapy.Request(url[0], callback=self.parse_product)
# 			request.meta['item'] = item
		#yield item			
			
# 	def parse_product(self, response):		
# 		item = response.meta['item']
# 		base_url = get_base_url(response)
# 		relative_url = response.xpath('//div[@class="product-meta"]/a/@href').extract()
# 		url = [urljoin_rfc(base_url,ru) for ru in relative_url]
# 		request = scrapy.Request(url[0], callback=self.parse_specs)
# 		request.meta['item'] = item
# 		yield request
# 	
# 	def parse_specs(self, response):
# 		item = response.meta['item']
# 		rows = response.xpath('//table[@class="wheel-specs"]/tbody/tr/td')
# 		wheel_size = rows.re('\d\d" x \d\d"')
# 		item['Option1_Name'] = 'Size'
# 		item['Option1_Value'] = sorted(set(wheel_size))
# 		yield item
