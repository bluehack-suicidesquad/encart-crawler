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
        'http://www.supermercadosguanabara.com.br/produtos/7'

    ]

    def parse(self, response):
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
            }