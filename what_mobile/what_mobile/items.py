# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WhatMobileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mobile_name = scrapy.Field()
    price_pkr = scrapy.Field()
    price_usd = scrapy.Field()
    rating = scrapy.Field()
    os = scrapy.Field()
    ui = scrapy.Field()
    dimensions = scrapy.Field()
    weight = scrapy.Field()
    sim = scrapy.Field()
    colors = scrapy.Field()
    band_2G = scrapy.Field()
    band_3G = scrapy.Field()
    band_4G = scrapy.Field()
    cpu = scrapy.Field()
    chipset = scrapy.Field()
    gpu = scrapy.Field()
    technology = scrapy.Field()
    size = scrapy.Field()
    resolution = scrapy.Field()
    protection = scrapy.Field()
    extra_features = scrapy.Field()
    built_in = scrapy.Field()
    card = scrapy.Field()
    main = scrapy.Field()
    features = scrapy.Field()
    front = scrapy.Field()
    wlan = scrapy.Field()
    bluetooth = scrapy.Field()
    gps = scrapy.Field()
    usb = scrapy.Field()
    nfc = scrapy.Field()
    data = scrapy.Field()
    sensors = scrapy.Field()
    audio = scrapy.Field()
    browser = scrapy.Field()
    messaging = scrapy.Field()
    games = scrapy.Field()
    torch = scrapy.Field()
    extra = scrapy.Field()
    capacity = scrapy.Field()
