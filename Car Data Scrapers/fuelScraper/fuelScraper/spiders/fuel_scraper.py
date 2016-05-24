import scrapy
import urlparse
from fuelScraper.items import FuelscraperItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class FuelScraper(scrapy.Spider):
	name = 'fuel'
	allowed_domains = ['fueloffroad.com']
	start_urls = [
		'http://www.fueloffroad.com/fuel-one-piece-b-1297.htm',
	 	'http://www.fueloffroad.com/fuel-two-piece-b-1296.htm'
	]
	
	def parse(self,response):
		base_url = get_base_url(response)
		for sel in response.xpath('//div[@class="row"]/div[@class="products-list small-6 medium-6 large-4 columns"]'):
			item = FuelscraperItem()
			item['Type'] = 'Rims'
			item['Vendor'] = 'Fuel'
			item['Option1_Name'] = 'Size'
			item['Option2_Name'] = 'Color'
			item['Option3_Name'] = 'Wheels'
			item['Option3_Value'] = '2,4,5,6'
			item['Image_Src'] = sel.xpath('a/img/@src').extract()
			item['Title'] = sel.xpath('a/img/@alt').extract()
			relative_url = sel.xpath('a/@href').extract()
 			url = [urljoin_rfc(base_url,ru) for ru in relative_url]
			request = scrapy.Request(url[0], callback=self.parse_product)
			request.meta['item'] = item
 			yield request			
			
	def parse_product(self, response):		
		item = response.meta['item']		
		finishes = response.xpath('//div[@class="small-12 medium-8"]/p/text()')
		item['Option2_Value'] = finishes.extract()
		sizes = sorted(set(response.xpath('//div[@id="detail-middle"]/div/div/p/text()').re('(\d\dx\d\d+|\d\d\.\dx\d\d|\d\dx\d\.\d+|\d\dx\d+)')))
		item['Option1_Value'] = [x for x in sizes if x != ""]
		if len(item['Option1_Value']) < 1:
			li = response.xpath('//ul[@class="related-specs detail-thumbs small-block-grid-4 medium-block-grid-6 large-block-grid-8"]/li/a/h3/text()').extract()
			item['Option1_Value'] = li
		yield item

