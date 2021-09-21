#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STEP 2
Takes the list of urls in the json files and downloads the html files to local drive
Start with: scrapy runspider ReviewsCollector.py

"""

import scrapy
import json

class ReviewsCollector(scrapy.Spider):

    def start_requests(self):
        with open("data/books.json") as f:
            self.data = json.load(f)
            for item in self.data:
                if (item['url'] is not None):
                    yield scrapy.Request(url=item['url'], headers={'Referer':'http://www.google.com/'}, callback=self.parse)


    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open('data/reviews/' + filename, 'wb+') as f:
            f.write(response.body)