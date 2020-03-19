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
        rows = response.xpath(
            '//div[@class="s-include-content-margin s-border-bottom s-latency-cf-section"]')
        for row in rows:
            yield Request(response.url, callback=self.get_data, meta={'row': row}, dont_filter=True)

    def get_data(self, response):
        l = ItemLoader(item=AmazonBooksItem(), response=response)
        row = response.meta.get('row')
        book_name = row.xpath(
            './/span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract_first()
        img = row.xpath(
            './/div[@class="a-section aok-relative s-image-fixed-height"]/img/@src').extract_first()
        author = row.xpath(
            './/div[@class="a-row a-size-base a-color-secondary"]/span[@dir="auto" and text()="by "][1]/following-sibling::*[1]/text()').extract()

        l.add_value('book_name', book_name, MapCompose(str.strip))
        l.add_value('img', img, MapCompose(str.strip))
        l.add_value('author', author, MapCompose(str.strip))

        return l.load_item()
