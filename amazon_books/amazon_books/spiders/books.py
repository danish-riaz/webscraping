# -*- coding: utf-8 -*-
import scrapy
from amazon_books.items import AmazonBooksItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.http import Request


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%211000%2Cn%3A3&page=2&qid=1584500043&ref=lp_3_pg_2']

    def parse(self, response):
        books_name = response.css(
            '.a-color-base.a-text-normal::text').extract()
        images = response.css('.s-image').xpath('.//@src').extract()
        authors = authors = response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "sg-col-12-of-28", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-secondary", " " ))]')
