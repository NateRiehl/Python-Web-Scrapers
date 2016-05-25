import time
import scrapy
import urlparse
from americanScraper.items import AmericanscraperItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import FormRequest
from selenium import webdriver
import selenium.webdriver.chrome.service as service

class AmericanSpider(scrapy.Spider):
	name = 'american'
	allowed_domains = ['americanforcewheels.com']
	start_urls = [
		'http://americanforcewheels.com/index.php/en/wheels-collection'
	]
		
	def parse(self,response):
		self.driver = webdriver.Chrome()
		self.driver.get('http://americanforcewheels.com/index.php/en/wheels-collection')
		i = 0
		while i < 5000:
			self.driver.execute_script("window.scrollTo(0,  "+ str(i + 50)+");")
			i = i + 100
			time.sleep(1)
		wheels = self.driver.find_elements_by_class_name('wheelsBox')
		base_url = get_base_url(response)
		for wheel in wheels:
			item = AmericanscraperItem()
			relative_url = wheel.get_attribute('href')
			item['Type'] = 'Rims'
			item['Vendor'] = 'American Force'
			item['Title'] = wheel.text
			img = wheel.find_element_by_tag_name('img')
			item['ImageSrc'] = img.get_attribute('src')
			request = scrapy.Request(relative_url, callback=self.parse_product)
			request.meta['item'] = item
			yield request		
			
	def parse_product(self, response):		
		item = response.meta['item']
		specs = response.xpath('//div[@class="fury"]/div[@class="tabe1"]/span/text()').re('\d\d"\*\d\d"|\d\d"\*\d"|\d\d"\*\d\.\d"|\d\d"\*\d\.\d\d"|\d\d\.\d"\*\d\d"|\d\d\.\d"\*\d\.\d"|\d\d\.\d"\*\d\.\d\d"|\d\d"')
		item['Option1Name'] = 'Size'
		item['MultipleOptionValues1'] = sorted(set(specs))
		item['Option2Name'] = 'Color'
		item['MultipleOptionValues2'] = 'Specify Color in Comments'
		item['Option3Name'] = 'Wheels'
		item['MultipleOptionValues3'] = '2,4,5,6'
		yield item
# 	
# 	def parse_specs(self, response):
# 		item = response.meta['item']
# 		rows = response.xpath('//table[@class="wheel-specs"]/tbody/tr/td')
# 		wheel_size = rows.re('\d\d" x \d\d"')
# 		item['Option1_Name'] = 'Size'
# 		item['Option1_Value'] = sorted(set(wheel_size))
# 		yield item
