# -*- coding: utf-8 -*-

import scrapy

class SugarBreadSpider(scrapy.Spider):
    name = "sugarbread"
    start_urls = [
        'http://www.superprix.com.br/carnes-e-pescados/aves?PS=500',
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
                'price': item.css('div.data .newPrice em').extract_first()
                    .replace('<em>R$ ','')
                    .replace('</em>',''),
                'market': 'superprix',
                'category': self.category
            }
