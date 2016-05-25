import scrapy
import urlparse
from kmc.items import KmcItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class KmcSpider(scrapy.Spider):
	name = 'kmc'
	allowed_domains = ['kmcwheels.com']
	start_urls = [
		'http://www.kmcwheels.com/wheels.cfm'
	]
	
	def parse(self,response):
		base_url = get_base_url(response)
		for ul in response.xpath('//ul[@class="small-block-grid-2 medium-block-grid-5 large-block-grid-6 list-wheels"]'):
			for li in ul.xpath('li'):
				item = KmcItem()
				title = li.xpath('a/div/div[@class="product-name"]/text()').extract()
				item['Title'] = title[0].strip()
				item['Type'] = 'Rims'
				item['Vendor'] = 'KMC Wheels'
				item['Option2Name'] = 'Colors'
				finishes = li.xpath('a/div/div[@class="product-finish"]/text()').extract()
				item['MultipleOptionValues2'] = finishes[0].strip()
				item['Option3Name'] = 'Wheels'
				item['MultipleOptionValues3'] = '2,4,5,6'
 				img = li.xpath('a/div[@class="image"]/img/@data-original').extract()
 				item['ImageSrc'] = img[0]
 				relative_url = li.xpath('a/@href').extract()
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
		wheel_size = rows.re('\d\d" x \d\d"|\d\d" x \d"|\d\d" x \d\.\d"')
		item['Option1Name'] = 'Size'
		item['MultipleOptionValues1'] = sorted(set(wheel_size))
		yield item
