#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STEP 3: Loading the json file, finding all the corresponding local html files, parsing the html and 
merging the data into a reviews.json 
Start with: scrapy runspider ReviewsParser.py -O data/reviews.json
"""

import scrapy
from bs4 import BeautifulSoup
import json
import os

LOCAL_FOLDER = 'moodybooks/data/reviews'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ReviewsParser(scrapy.Spider):

    def start_requests(self):
        with open("data/books.json") as f:
            self.data = json.load(f)
            for item in self.data:
                if (item['url'] is not None):
                    url = f"file://{BASE_DIR}/{LOCAL_FOLDER}/" + item['url'].split("/")[-1] + '.html'
                    yield scrapy.Request(
                            url=url,
                            meta={'number': item['number'], 'author': item['author'], 'title': item['title'], 'remote_url': item['url']},
                            callback=self.parse)


    def parse(self, response):
 
        soup = BeautifulSoup(response.body, "lxml") 

        for script in soup(["script", "style"]):
            script.extract()

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