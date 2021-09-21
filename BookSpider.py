#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STEP 1
Retrieves data (review url, title, author) from the main list of books
and stores it in a json file
Start with: scrapy runspider BookSpider.py -O data/books.json
"""

import scrapy

class BookSpider(scrapy.Spider):
    start_urls = [
        'https://www.theguardian.com/books/2019/sep/21/best-books-of-the-21st-century',
    ]

    def parse(self, response):
        for books in response.css('div.article-body-commercial-selector'):
            node = 0
            for nr in range(1, 101):
                node += 1
                yield{
                    'number': books.xpath('h2[{}]/text()'.format(node)).get(),
                    'title': books.xpath('h2[{}]/strong/text()'.format(node + 1)).get(),
                    'author': books.xpath('h2[{}]/text()'.format(node + 2)).get(),
                    #'text': books.xpath('p[{}]/text()'.format(nr + 1)).get(),
                    'url': books.xpath('p[{}]/em/a/@href'.format(nr + 1)).get()
                }
                node = node + 2