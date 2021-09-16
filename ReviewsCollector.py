#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start with: scrapy runspider ReviewsCollector.py

main artcile: //*[@id="maincontent"]
intro: /html/body/article/div/div/div[5]/div
author: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/address/div/a
date: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/div

sel = response.xpath(//*[@id="maincontent"])
''.join(selector.select("//body//text()").extract()).strip()


"""

import scrapy
import json

class ReviewsCollector(scrapy.Spider):
    name = 'books'
    urls = [
    ]

    def start_requests(self):
        with open("data/books.json") as f:
            self.data = json.load(f)
            for item in self.data:
                print(item['url'])
                if (item['url'] is not None):
                    yield scrapy.Request(url=item['url'], headers={'Referer':'http://www.google.com/'}, callback=self.parse)


    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open('data/reviews/' + filename, 'wb+') as f:
            f.write(response.body)