#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:47:56 2021

@author: fred
https://docs.scrapy.org/en/latest/intro/overview.html
Started with: scrapy runspider BookSpider.py -O books.json

/html/body/article/div/div/div[9]/main/main/div[1]/div/p[3]/em[2]/a
"""

import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'https://www.theguardian.com/books/2019/sep/21/best-books-of-the-21st-century',
    ]

    def parse(self, response):
        for books in response.css('div.article-body-commercial-selector'):
            node = 0
            for nr in range(1, 100):
                node += 1
                
            #for url in books.css('a::attr(href)'):
                yield{
                    'number': books.xpath('h2[{}]/text()'.format(node)).get(),
                    'title': books.xpath('h2[{}]/strong/text()'.format(node + 1)).get(),
                    'author': books.xpath('h2[{}]/text()'.format(node + 2)).get(),
                    #'text': books.xpath('p[{}]/text()'.format(nr + 1)).get(),
                    'url': books.xpath('p[{}]/em/a/@href'.format(nr + 1)).get()
                }
                node = node + 2