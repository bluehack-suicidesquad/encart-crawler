# -*- coding: utf-8 -*-

import scrapy
import json

class SugarbreadSpider(scrapy.Spider):
    name = "sugarbread"

    start_urls = [
        'https://api.gpa.digital/pa/products/list/secoes/C4233/limpeza?storeId=501&qt=36&s=&ftr=&p=&rm=&gt=list',

    ]

    def parse(self, response):

        data = []
        jsonresponse = json.loads(response.body_as_unicode())

        # yield {

        data_content = jsonresponse["content"]

        # }

        data_host = "https://www.paodeacucar.com"

        for products in data_content["products"]:
            yield {

            "Category": products["shelfList"][1]["name"],
            "Name": products["name"],
            "Price": products["currentPrice"],
            "Market": "Pao de Acucar",
            # "Image": products["mapOfImages"][0]["MEDIUM"],

            }
        #