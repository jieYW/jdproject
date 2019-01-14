import scrapy
from jdproject.items import ProductTypeItem


class JDProductTypeSpider(scrapy.Spider):
    name = 'jdpt'

    start_urls = [
        'https://www.jd.com/allSort.aspx'
    ]

    def parse(self, response):
        ptItem1 = ProductTypeItem()
        ptItem2 = ProductTypeItem()
        ptItem3 = ProductTypeItem()
        # 一级类别
        for pta in response.css('div.category-item'):
            ptItem1['name'] = pta.css('div.mt span::text').extract_first()
            ptItem1url = pta.css('div.items .clearfix dt a::attr(href)').extract_first()
            ptItem1['pid'] = 0
            ptItem1['id'] = ptItem1url.split('/')[-1].split('.')[0].split('-')[0]
            # print(ptItem1)
            # 二级类别
            for ptb in pta.css('div.items .clearfix'):
                ptItem2['name'] = ptb.css('dt a::text').extract_first()
                ptItem2url = ptb.css('dt a::attr(href)').extract_first()
                ptItem2['url'] = ptItem2url
                '''
                if ptItem1url.count('-') > 0:
                    ptItem2['pid'] = ptItem2url.split('/')[-1].split('.')[0].split('-')[0]
                    ptItem2['id'] = ptItem2url.split('/')[-1].split('.')[0].split('-')[1]
                '''
                # print(ptItem2)
                # 三级类别
                for ptc in ptb.css('dd a'):
                    ptItem3['name'] = ptc.xpath('text()').extract_first()
                    ptItem3url = ptc.xpath("@href").extract_first()
                    ptItem3['url'] = ptItem3url
                    try:
                        if ptItem3url.count('?') > 0:
                            ppids = ptItem3url.split('?')[-1].split('=')[-1].split(',')
                            if len(ppids) == 3:
                                ptItem3['id'] = ppids[2]
                                ptItem3['pid'] = ppids[1]
                                ptItem2['id'] = ppids[1]
                                ptItem2['pid'] = ppids[0]
                                ptItem1['id'] = ppids[0]
                            elif len(ppids) == 2:
                                #print(ppids)
                                ptItem2['id'] = ppids[1]
                                ptItem2['pid'] = ppids[0]
                                ptItem1['id'] = ppids[0]
                            else:
                                #print(ptItem3url)
                                if ptItem3url.count('&'):
                                    ttids = ptItem3url.split('&')[0].split('?')[-1].split('=')[-1].split(',')
                                    if len(ttids) == 2:
                                        # print(ttids)
                                        ptItem2['id'] = ttids[1]
                                        ptItem2['pid'] = ttids[0]
                                        ptItem1['id'] = ttids[0]
                        else:
                            #print(ptItem3url)
                            if ptItem3url.count('-') > 0:
                                ptItem2['id'] = ptItem3url.split('/')[-1].split('.')[0].split('-')[1]
                                ptItem2['pid'] = ptItem3url.split('/')[-1].split('.')[0].split('-')[0]
                                ptItem1['id'] = ptItem3url.split('/')[-1].split('.')[0].split('-')[0]

                    except Exception:
                        #print(ptItem3url)
                        pass

                    print(ptItem3)
                    yield ptItem3
                print("----------------")
                print(ptItem2)
                yield ptItem2
            print("++++++++++++++++++++++++++++++++++")
            print(ptItem1)
            yield ptItem1











