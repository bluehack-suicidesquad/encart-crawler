import scrapy

class MundialSpider(scrapy.Spider):
    name = "mundial"
    def start_requests(self):
        urls = [
            'http://www.supermercadosmundial.com.br/ofertas/bebidas?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/bebidas-alcoolicas?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/biscoitos-e-bonbonniere?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/cereais-e-farinaceos?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/conservas?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/light-e-diet?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/matinais?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/massas?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/sobremesas?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/higiene?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/limpeza?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/pet-shop?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/bazar?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/laticinios-e-frios?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/peixaria?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/acougue?format=json&page=1',
            'http://www.supermercadosmundial.com.br/ofertas/congelados?format=json&page=1'
        ]
        for url in urls:
            page = 1
            yield scrapy.Request(url=url, callback=self.parse,meta={'page': page})


    def parse(self, response):
        page = response.meta['page']
        for item in response.css('div#ofertas-content div.product'):
            yield {
                'name': item.css('span.link-offers span.name-product::text')
                    .extract_first(),
                'image': item.css('span.link-offers img.img-responsive::attr(src)').extract_first(),
                'price': item.css('span.link-offers span.price-product i::text')
                    .extract_first() + ' ' + item.css('span.link-offers span.price-product strong::text')
                    .extract_first() + item.css('span.link-offers span.price-product strong sup::text')
                    .extract_first(),
                'page': page,
                'market': 'Mundial'
            }
        next_page = response.css('div.ofertas-content button.load-more::attr(disabled)').extract_first()
        if next_page is None:
            auxpage = page + 1
            next_page = response.url.replace('&page=' + str(page),'&page=' + str(auxpage)) 
            yield scrapy.Request(next_page, callback=self.parse,meta={'page': auxpage})