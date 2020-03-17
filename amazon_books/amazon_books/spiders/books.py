# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
