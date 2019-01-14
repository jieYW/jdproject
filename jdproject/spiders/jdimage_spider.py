import scrapy
from jdproject.items import JdprojectItem


class JDImageSpider(scrapy.Spider):
    name = 'jdimage'

    start_urls = [
        'https://www.jd.com'
    ]

    def parse(self, response):
        item = JdprojectItem()
        item['name'] = response.css('.cate_menu_item a::text').extract()
        item['url'] = response.css('.cate_menu_item a::attr(href)').extract()
        print(item)


