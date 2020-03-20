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
        authors = response.xpath(
            '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/following-sibling::div')
        for row, author in zip(rows, authors):
            yield Request(response.url, callback=self.get_data, meta={'row': row, 'author': author}, dont_filter=True)

    def get_data(self, response):
        l = ItemLoader(item=AmazonBooksItem(), response=response)
        row = response.meta.get('row')
        author = response.meta.get('author')
        book_name = row.xpath(
            './/span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract_first()
        img = row.xpath(
            './/div[@class="a-section aok-relative s-image-fixed-height"]/img/@src').extract_first()
        author = author.xpath('.//*/text()').extract()

        rating = response.xpath(
            '//div[@class="a-section a-spacing-none a-spacing-top-micro"]/div[@class="a-row a-size-small"]/span[1]/@aria-label').extract()
        rating_by = response.xpath(
            '//div[@class="a-section a-spacing-none a-spacing-top-micro"]/div[@class="a-row a-size-small"]/span[2]/@aria-label').extract()

        l.add_value('book_name', book_name, MapCompose(str.strip))
        l.add_value('img', img, MapCompose(str.strip))
        l.add_value('author', author, MapCompose(str.strip))
        l.add_value('rating', rating)
        l.add_value('rating_by', rating_by)

        return l.load_item()
