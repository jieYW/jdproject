import scrapy
from jdproject.items import ProductItem
from scrapy_splash import SplashRequest


class ProductSpider(scrapy.Spider):
    name = 'jdproduct'
    start_urls = [
        'https://list.jd.com/list.html?cat=6233,6271,7063',
        #'https://list.jd.com/list.html?cat=6233,6271,7063&page=9&sort=sort_rank_asc&trans=1&JL=6_0_0',
    ]

    # request需要封装成SplashRequest
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': '0.5'})

    def parse(self, response):
        productItem = ProductItem()
        for gl in response.css('li.gl-item'):
            # print(gl)
            productItem['name'] = gl.css('.p-name em::text').extract_first().strip()
            productItem['id'] = int(gl.xpath('div[@class="gl-i-wrap j-sku-item"]//@data-sku').extract_first())
            productItem['shopId'] = int(gl.xpath('div[@class="gl-i-wrap j-sku-item"]//@jdzy_shop_id').extract_first())
            productItem['brandId'] = int(gl.xpath('div[@class="gl-i-wrap j-sku-item"]//@brand_id').extract_first())
            # 图片地址
            lazyImg = gl.css('div.p-img img::attr(data-lazy-img)').extract_first()
            if lazyImg is None:
                lazyImg = gl.css('div.p-img img::attr(src)').extract_first()
            productItem['imgUrl'] = lazyImg
            productItem['detailPage'] = "//item.jd.com/" + str(productItem['id']) + ".html"
            try:
                price = float(gl.xpath('div//strong[@class="J_price"]/i/text()').extract_first())
                productItem['price'] = int(price * 100)
            except Exception:
                # 暂无报价
                productItem['price'] = 0

            # print(productItem)
            yield productItem

        next_page = response.xpath('//a[@class="pn-next"]//@href').extract_first()
        if next_page is not None:
            next_page = "https://list.jd.com" + next_page
            print(next_page)
            next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield SplashRequest(next_page, self.parse, args={'wait': '0.5'})

