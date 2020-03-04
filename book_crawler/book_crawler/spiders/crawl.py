# -*- coding: utf-8 -*-
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request


class CrawlSpider(Spider):
    name = 'crawl'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://books.toscrape.com/')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath("//h3/a/@href").extract()
        for book in books:
            book_url = 'http://books.toscrape.com/' + book
            yield Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        pass
    # start_urls = ['http://books.toscrape.com/']

    # # rule = (Rule(LinkExtractor(deny_domains='google.com'),
    # #         callback='book_crawl', follow=True),)
    # rule = (Rule(LinkExtractor(allow='music'),
    #              callback='book_crawl', follow=True))

    # def parse(self, response):
    #     pass

    # def book_crawl(self, response):
    #     yield {
    #         'URL': response.url
    #     }
