#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:47:56 2021

@author: fred
https://docs.scrapy.org/en/latest/intro/overview.html
Started with: scrapy runspider BookSpider.py -o books.jl
.article-body-commercial-selector
html.src-focus-disabled body article.dcr-153y9kh div.dcr-1o52fwf div.dcr-1xvhifk div.dcr-185kcx9 main.dcr-lg1c4h main.dcr-krkkhw div#maincontent.dcr-k3st4d div.article-body-commercial-selector.article-body-viewer-selector.dcr-bjn8wh
"""

import scrapy


class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'https://www.theguardian.com/books/2019/sep/21/best-books-of-the-21st-century',
    ]

    def parse(self, response):
        for books in response.css('div.article-body-commercial-selector'):
            yield {
                'author': books.xpath('span/small/text()').get(),
                'text': books.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


