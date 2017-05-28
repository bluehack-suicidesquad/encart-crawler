# -*- coding: utf-8 -*-

import scrapy
import json

class SugarbreadSpider(scrapy.Spider):
    name = "sugarbread"

    start_urls = [
        'https://api.gpa.digital/pa/products/list/secoes/C4233/limpeza?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/products/list/secoes/C4215/bebidas?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/products/list/secoes/C4226/carnes?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/products/list/secoes/C4229/bebes?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/products/list/secoes/C4223/alimentos?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/products/list/secoes/C4231/perfumaria?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',
        'https://api.gpa.digital/pa/prgitstoducts/list/secoes/C4205/feira?storeId=501&qt=50&s=&ftr=&p=&rm=&gt=list',

    ]

    def parse(self, response):

        jsonresponse = json.loads(response.body_as_unicode())
        data_content = jsonresponse["content"]
        data_host = "https://www.paodeacucar.com"

        for products in data_content["products"]:
            yield {

            "category": products["shelfList"][1]["name"],
            "name": products["name"],
            "price": products["currentPrice"],
            "market": "Pao de Acucar",
            "image": data_host + products["mapOfImages"]["0"]["MEDIUM"],

            }

        """
        Código para poder fazer o post para o datastorage

        file = open('file/path/file.json', 'r')
        file_obj = file.read()
        data = file_ojb
        response = request.post('https://encart.io/endpoint', data)

        """

