# -*- coding: utf-8 -*-

import scrapy

class SuperprixSpider(scrapy.Spider):
    name = "superprix"
    start_urls = [
        'http://www.superprix.com.br/carnes-e-pescados/aves?PS=500',
        'http://www.superprix.com.br/carnes-e-pescados/bovinas?PS=500',
        'http://www.superprix.com.br/carnes-e-pescados/suinas?PS=500',
        'http://www.superprix.com.br/carnes-e-pescados/peixes?PS=500',
        'http://www.superprix.com.br/carnes-e-pescados/frutos-do-mar?PS=500',
        'http://www.superprix.com.br/carnes-e-pescados/linguicas?PS=500',
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
