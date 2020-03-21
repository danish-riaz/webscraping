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
        rows = rows = response.xpath(
            '//div[@class="s-include-content-margin s-border-bottom s-latency-cf-section"]')
        for row in rows:
            img_link = row.xpath(
                './/div[@class="sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"]//span/a/div/img/@src').extract()
            book_name = row.xpath(
                './/div[@class="sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"]//h2//a//span/text()').extract()
            author = row.xpath('.').css(
                '.sg-col-12-of-28 .a-color-secondary').css('::text').extract()
            author = [each.strip() for each in author]
            author = list(filter(None, author))
            author = ''.join(author)
            author = author.replace("by", "")
            rating = row.xpath('.').css(
                '.sg-col-12-of-28 .aok-align-bottom').xpath('./span/text()').extract()
            by_users = row.xpath('.').css(
                '.sg-col-12-of-28 .a-link-normal .a-size-base').xpath('./text()').extract()
