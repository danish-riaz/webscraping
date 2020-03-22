# -*- coding: utf-8 -*-
import scrapy
# from amazon_books.items import AmazonBooksItem
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import MapCompose
from scrapy.http import Request


class BooksSpider(scrapy.Spider):
    name = 'books'
    page_no = 2
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%211000%2Cn%3A3&page=2&qid=1584500043&ref=lp_3_pg_2']

    def parse(self, response):
        rows = rows = response.xpath(
            '//div[@class="s-include-content-margin s-border-bottom s-latency-cf-section"]')
        prices = response.css('.sg-col-20-of-28 .sg-col-4-of-32 .sg-col-inner')
        for row, price in zip(rows, prices):
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

            temp = []
            l_p = price.xpath(
                './/div[@class="a-row"]/a/span[@class="a-price"]/span[@class="a-offscreen"]/text()').extract()
            label = price.xpath('.').css(
                '.a-link-normal.a-text-bold::text').extract()
            label = [each.strip() for each in label]
            for a, b in zip(label, l_p):
                temp.append(a)
                temp.append(b)

            yield {'img_link': img_link,
                   'book_name': book_name,
                   'author': author,
                   'rating': rating,
                   'by_users': by_users,
                   'temp': temp
                   }

            next_page = 'https://www.amazon.com/s?rh=n%3A283155%2Cn%3A%211000%2Cn%3A3&page=' + \
                str(BooksSpider.page_no) + '&qid=1584500043&ref=lp_3_pg_2'
            if BooksSpider.page_no <= 50:
                BooksSpider.page_no += 1
                yield Request(next_page, callback=self.parse)
