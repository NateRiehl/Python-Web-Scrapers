import scrapy
import urlparse
from motometal.items import MotometalItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class MotoSpider(scrapy.Spider):
	name = 'moto'
	allowed_domains = ['motometalwheels.com']
	start_urls = [
		'http://www.motometalwheels.com/wheels.cfm'
	]
	
	def parse(self,response):
		base_url = get_base_url(response)
		for sel in response.xpath('//div[@class="small-12 columns"]/ul/li'):
			item = MotometalItem()
			item['Type'] = 'Rims'
			item['Vendor'] = 'Moto Metal'
			item['Option3_Name'] = 'Wheels'
			item['Option3_Value'] = '2,4,5,6'
			item['Title'] = sel.xpath('a/div[@class="meta"]/div[@class="product-name"]/text()').extract()
			title = sel.xpath('a/div[@class="meta"]/div[@class="product-finish"]/text()').extract()
			item['Option2_Name'] = 'Color'
			item['Option2_Value'] = title[0]
			relative_url = sel.xpath('a/@href').extract()
 			url = [urljoin_rfc(base_url,ru) for ru in relative_url]
			request = scrapy.Request(url[0], callback=self.parse_product)
			request.meta['item'] = item
			yield request			
			
	def parse_product(self, response):		
		item = response.meta['item']
		base_url = get_base_url(response)
		relative_url = response.xpath('//div[@class="product-meta"]/a/@href').extract()
		url = [urljoin_rfc(base_url,ru) for ru in relative_url]
		request = scrapy.Request(url[0], callback=self.parse_specs)
		request.meta['item'] = item
		yield request
	
	def parse_specs(self, response):
		item = response.meta['item']
		rows = response.xpath('//table[@class="wheel-specs"]/tbody/tr/td')
		wheel_size = rows.re('\d\d" x \d\d"')
		item['Option1_Name'] = 'Size'
		item['Option1_Value'] = sorted(set(wheel_size))
		yield item
