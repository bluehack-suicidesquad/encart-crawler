import scrapy

class ZonaSulSpider(scrapy.Spider):
    name = "zonasul"
    start_urls = [
        'https://www.zonasul.com.br/WebForms/Lista-Facetada.aspx?lista=encarte&Pagina=1',
    ]

    def parse(self, response):
        for item in response.css('div.produtos li.liItemTemplate'):
            yield {
                'name': item.css('div.bloco_informacoes div.prod_info a::text').extract_first(),
                'image': item.css('div.prod_image img.img_thumb_list::attr(imgsrc160)').extract_first(),
                'price': item.css('div.bloco_informacoes div.prod_preco_qtd div.prod_preco p.preco_por ins::text').extract_first()
            }