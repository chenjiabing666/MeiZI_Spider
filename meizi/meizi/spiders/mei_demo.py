# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from meizi.items import MeiziItem
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
class MeiDemoSpider(CrawlSpider):
    name = "mei_demo"
    #allowed_domains = ["mezi.com"]
    start_urls = ['http://www.mzitu.com/xinggan',
                  "http://www.mzitu.com/japan",
                  "http://www.mzitu.com/taiwan",
                  "http://www.mzitu.com/mm"

                  ]
    rules={
        Rule(LinkExtractor(allow="http://www.mzitu.com/xinggan/page/\d+",restrict_xpaths="//div[@class='nav-links']"),follow=True),
        Rule(LinkExtractor(allow="http://www.mzitu.com/\d+",restrict_xpaths="//div[@class='postlist']"),follow=True),
        Rule(LinkExtractor(allow="http://www.mzitu.com/\d+/\d+",restrict_xpaths="//div[@class='pagenavi']"),follow=True,callback='parse_item')

    }

    def parse_item(self,response):
        item=MeiziItem()
        try:
            item['img_urls'] = response.xpath("//div[@class='main-image']/p/a/img/@src")[0].extract()
            item['img_name'] = response.xpath("//div[@class='currentpath']/a[2]/text()")[0].extract()
            yield item
        except Exception:
            pass






