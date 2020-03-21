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
        l2 = []
        for author in authors:
            author = author.xpath('.//*/text()').extract()
            author = [each.strip() for each in author]
            author = ''.join(author)
            l2.append(author)
        l2 = list(filter(None, l2))
        l2 = [each.replace("by", "")for each in l2]

        first_avalibility = response.css(
            '.a-spacing-top-small .a-link-normal.a-text-bold::text').extract()
        first_avalibility = [each.strip() for each in first_avalibility]

        for book_name, image, author in zip(books_name, images, l2):
            # print(book_name, image, author)
            yield Request(response.url, callback=self.print_data, meta={'book_name': book_name, 'image': image, 'author': author}, dont_filter=True)

    def print_data(self, response):
        item_obj = ItemLoader(item=AmazonBooksItem(), response=response)

        book_name = response.meta.get('book_name')
        image = response.meta.get('image')
        author = response.meta.get('author')

        item_obj.add_value('book_name', book_name)
        item_obj.add_value('image', image)
        item_obj.add_value('author', author)

        return item_obj.load_item()
