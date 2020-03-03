# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            author = quote.xpath(
                ".//*[@class='author']/text()").extract_first()
            tags = quote.xpath(
                ".//*[@itemprop='keywords']/@content").extract_first()

            yield{
                'Text': text,
                'Author': author,
                'Tags': tags
            }

        next_page = response.xpath(
            ".//*[@class='next']/a/@href").extract_first()
        abs_next_page = response.urljoin(next_page)

        yield scrapy.Request(abs_next_page)
