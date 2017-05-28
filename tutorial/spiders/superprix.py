# -*- coding: utf-8 -*-

import scrapy

class SuperprixSpider(scrapy.Spider):
    name = "superprix"
    start_urls = [
        'http://www.superprix.com.br/carnes-e-pescados/',
        'http://www.superprix.com.br/bebidas/'
    ]

    def parse(self, response):

        self.category = ''

        self.category = response.css('.bread-crumb li.last a::attr(title)').extract_first()

        for item in response.css('div.prateleira > ul > li:not(.helperComplement)'):
            yield {
                'name': item.css('a.productImage::attr(title)')
                    .extract_first(),
                'image': item.css('a.productImage img::attr(src)')
                    .extract_first(),
                'price': item.css('div.data .newPrice em').extract_first(),
                'market': 'superprix',
                'category': self.category
            }
