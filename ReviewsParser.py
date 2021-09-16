#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start with: scrapy runspider ReviewsParser.py

main artcile: //*[@id="maincontent"]
intro: /html/body/article/div/div/div[5]/div
author: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/address/div/a
date: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/div

sel = response.xpath(//*[@id="maincontent"])
''.join(selector.select("//body//text()").extract()).strip()


"""

import scrapy
import json
import os
#/home/fred/dev/mda512/moodybooks/data/reviews/wolf-hall-hilary-mantel.html

LOCAL_FOLDER = 'moodybooks/data/reviews'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ReviewsParser(scrapy.Spider):
    name = 'books'
    urls = [
    ]

    def start_requests(self):
        with open("data/books.json") as f:
            self.data = json.load(f)
            for item in self.data:
                print(item['url'])
                if (item['url'] is not None):
                    url = f"file://{BASE_DIR}/{LOCAL_FOLDER}/" + item['url'].split("/")[-1] + '.html'
                    yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print(response.url)
"""         with open('data/reviews/' + filename, 'wb+') as f:
            f.write(response.body) """