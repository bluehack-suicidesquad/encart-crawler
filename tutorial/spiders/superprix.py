# -*- coding: utf-8 -*-

import scrapy

class SuperprixSpider(scrapy.Spider):
    name = "superprix"
    start_urls = [
        'http://www.superprix.com.br/carnes-e-pescados'
    ]

    def parse(self, response):
        for item in response.css('div.prateleira'):
            yield {
                'name': item.css('a.productImage::attr(title)').extract_first(),
                'image': item.css('a.productImage img::attr(src)').extract_first(),
                'price': item.css('span.newPrice em').extract_first().replace('<em>R$ ','').replace('</em>','')
            }
