import scrapy

class GuanabaraSpider(scrapy.Spider):
    name = "guanabara"
    start_urls = [
        'http://www.supermercadosguanabara.com.br/produtos/1',
        'http://www.supermercadosguanabara.com.br/produtos/2',
        'http://www.supermercadosguanabara.com.br/produtos/3',
        'http://www.supermercadosguanabara.com.br/produtos/4',
        'http://www.supermercadosguanabara.com.br/produtos/5',
        'http://www.supermercadosguanabara.com.br/produtos/6',
        'http://www.supermercadosguanabara.com.br/produtos/7',
        'http://www.supermercadosguanabara.com.br/produtos/8',
        'http://www.supermercadosguanabara.com.br/produtos/9',
        'http://www.supermercadosguanabara.com.br/produtos/10',
        'http://www.supermercadosguanabara.com.br/produtos/11',
        'http://www.supermercadosguanabara.com.br/produtos/12',
        'http://www.supermercadosguanabara.com.br/produtos/13',
        'http://www.supermercadosguanabara.com.br/produtos/14',
        'http://www.supermercadosguanabara.com.br/produtos/15',
        'http://www.supermercadosguanabara.com.br/produtos/16',
        'http://www.supermercadosguanabara.com.br/produtos/17',
        'http://www.supermercadosguanabara.com.br/produtos/18',
        'http://www.supermercadosguanabara.com.br/produtos/19',
        'http://www.supermercadosguanabara.com.br/produtos/20',
        'http://www.supermercadosguanabara.com.br/produtos/21',
        'http://www.supermercadosguanabara.com.br/produtos/22',
        'http://www.supermercadosguanabara.com.br/produtos/23',
        'http://www.supermercadosguanabara.com.br/produtos/24',
        'http://www.supermercadosguanabara.com.br/produtos/25',
        'http://www.supermercadosguanabara.com.br/produtos/26'
    ]

    def parse(self, response):
        self.category = ''

        self.category = response.css('div.products-bar div.title h3::text').extract_first()
        for item in response.css('div.products-list div.item'):
            yield {
                'name': item.css('div.name::text')
                    .extract_first(),
                'image': item.css('div.image::attr(style)')
                    .extract_first()
                    .replace('background-image: url(\'','')
                    .replace('\');',''),
                'price': item.css('span.number::text')
                    .extract_first(),
                'category': self.category,
                'market': 'Guanabara'
            }