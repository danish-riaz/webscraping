# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h1 = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_etax = scrapy.Field()
    price_itac = scrapy.Field()
    tax = scrapy.Field()
    avalibility = scrapy.Field()
    reviews = scrapy.Field()
    des = scrapy.Field()
    image_urls = scrapy.Field()

    # def __repr__(self):
    #     return ""
