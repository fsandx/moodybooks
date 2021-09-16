#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Start with: scrapy runspider ReviewsParser.py -O data/reviews.json
main artcile: //*[@id="maincontent"]
intro: /html/body/article/div/div/div[5]/div
author: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/address/div/a
date: /html/body/article/div/div/div[8]/div/div/div/div[1]/div/div

sel = response.xpath(//*[@id="maincontent"])
''.join(selector.select("//body//text()").extract()).strip()


"""

import scrapy
from bs4 import BeautifulSoup
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
                #print(item['url'])
                if (item['url'] is not None):
                    url = f"file://{BASE_DIR}/{LOCAL_FOLDER}/" + item['url'].split("/")[-1] + '.html'
                    yield scrapy.Request(
                        url=url,
                        meta={'number': item['number'], 'author': item['author'], 'title': item['title'], 'remote_url': item['url']},
                        callback=self.parse)


    def parse(self, response):
    # print(response.url)
        #article = response.xpath('//*[@id="maincontent"]/text()').get()
        soup = BeautifulSoup(response.body, "lxml") 

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        yield {
            'number': response.meta['number'],
            'author': response.meta['author'],
            'title': response.meta['title'],
            'url': response.meta['remote_url'],
            'text': text
        }