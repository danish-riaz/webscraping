# -*- coding: utf-8 -*-
import scrapy
#from scrapy.loader import ItemLoader

#from quotes_spider.items import QuotesSpiderItem
from time import sleep
import random


class QuotesSpider(scrapy.Spider):

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        # item_obj = ItemLoader(item=QuotesSpiderItem(), response=response)

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            author = quote.xpath(
                ".//*[@class='author']/text()").extract_first()
            tags = quote.xpath(
                ".//*[@itemprop='keywords']/@content").extract_first()

            # item_obj.add_value('text', text)
            # item_obj.add_value('author', author)
            # item_obj.add_value('tags', tags)

            # return item_obj.load_item()
            yield{
                'Text': text,
                'Author': author,
                'Tags': tags
            }
            sleep(random.randrange(1, 3))

        next_page = response.xpath(
            ".//*[@class='next']/a/@href").extract_first()
        abs_next_page = response.urljoin(next_page)

        yield scrapy.Request(abs_next_page)
