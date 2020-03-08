# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.loader import ItemLoader
from what_mobile.item import WhatMobileItem


def first_element(response, name):
    return response.xpath('//*[@class="RowBG2"]/th[text()="' + name + '"]/following-sibling::td/text()').extract()


def after_first_element(response, name):
    return response.xpath('//*[@class="RowBG1"]/th[text()="' + name + '"]/following-sibling::td/text()').extract()


class MobileSpider(Spider):
    name = 'mobile'
    allowed_domains = ['whatmobile.com.pk']
    start_urls = ['http://whatmobile.com.pk/']

    def parse(self, response):
        brands = response.xpath(
            '//*[@class="verticalMenu"]/section[2]/ul/li/a/@href').extract()

        for brand in brands:
            brand_url = response.urljoin(brand)
            yield Request(brand_url, callback=self.brand_parse)
            break

    def brand_parse(self, response):
        print("**************************************INSIDE**************************************")
        prices = response.xpath('//*[@class="item"]/div/a[1]/@href').extract()
        for price in prices:
            mobile_url = 'https://www.whatmobile.com.pk' + price
            yield Request(mobile_url, callback=self.mobile_data)
            break

        # latests = response.xpath(
        #     '//*[@role="presentation"]/a/@href')[1].extract()
        # latests = 'https://www.whatmobile.com.pk/' + latests
        # latests = response.xpath('//*[@class="item"]/div/a[1]/@href').extract()
        # for latest in latests:
        #     mobile_url = 'http://whatmobile.com.pk' + latest
        #     yield Request(mobile_url, callback=self.mobile_data)

        # coming_soons = response.xpath(
        #     '//*[@role="presentation"]/a/@href')[2].extract()
        # coming_soons = 'https://www.whatmobile.com.pk/' + coming_soons
        # coming_soons = response.xpath(
        #     '//*[@class="item"]/div/a[1]/@href').extract()

        # for coming_soon in coming_soons:
        #     mobile_url = 'http://whatmobile.com.pk' + coming_soon
        #     yield Request(mobile_url, callback=self.mobile_data)

    def mobile_data(self, response):

        l = ItemLoader(text=WhatMobileItem(), response=response)

        mobile_name = response.xpath(
            '//h1[@class="hdng3"]/text()').extract_first()
        price_pkr = response.xpath('//*[@class="hdng"]/text()')[0].extract()
        price_usd = response.xpath('//*[@class="hdng"]/text()')[1].extract()
        rating = response.xpath(
            '//*[contains(@class, "rateit")]/@data-rateit-value')[0].extract()
        # Build
        os = first_element(response, "OS")
        ui = after_first_element(response, "UI")
        dimensions = after_first_element(response, "Dimensions")
        weight = after_first_element(response, "Weight")
        sim = after_first_element(response, "SIM")
        colors = after_first_element(response, "Colors")
        # Frequency
        band_2G = first_element(response, "2G Band")
        band_3G = after_first_element(response, "3G Band")
        band_4G = after_first_element(response, "4G Band")
        # Processor
        cpu = first_element(response, "CPU")
        chipset = after_first_element(response, "Chipset")
        gpu = after_first_element(response, "GPU")
        # Display
        technology = first_element(response, "Technology")
        size = after_first_element(response, "Size")
        resolution = after_first_element(response, "Resolution")
        protection = after_first_element(response, "Protection")
        extra_features = after_first_element(response, "Extra Features")
        # Memory
        built_in = first_element(response, "Built-in")
        card = after_first_element(response, "Card")
        # Camera
        main = first_element(response, "Main")
        features = after_first_element(response, "Features")
        front = after_first_element(response, "Front")
        # Connectivity
        wlan = first_element(response, "WLAN")
        bluetooth = after_first_element(response, "Bluetooth")
        gps = after_first_element(response, "GPS")
        usb = after_first_element(response, "USB")
        nfc = after_first_element(response, "NFC")
        data = after_first_element(response, "Data")
        # Features
        sensors = first_element(response, "Sensors")
        audio = after_first_element(response, "Audio")
        browser = after_first_element(response, "Browser")
        messaging = after_first_element(response, "Messaging")
        games = after_first_element(response, "Games")
        torch = after_first_element(response, "Torch")
        extra = after_first_element(response, "Extra")
        # Battery
        capacity = first_element(response, "Capacity")

        l.add_value('mobile_name', mobile_name)
        l.add_value('price_pkr', price_pkr)
        l.add_value('price_usd', price_usd)
        l.add_value('rating', rating)
        l.add_value('os', os)
        l.add_value('ui', ui)
        l.add_value('dimensions', dimensions)
        l.add_value('weight', weight)
        l.add_value('sim', sim)
        l.add_value('colors', colors)
        l.add_value('band_2G', band_2G)
        l.add_value('band_3G', band_3G)
        l.add_value('band_4G', band_4G)
        l.add_value('cpu', cpu)
        l.add_value('chipset', chipset)
        l.add_value('gpu', gpu)
        l.add_value('technology', technology)
        l.add_value('size', size)
        l.add_value('resolution', resolution)
        l.add_value('protection', protection)
        l.add_value('extra_features', extra_features)
        l.add_value('built_in', built_in)
        l.add_value('card', card)
        l.add_value('main', main)
        l.add_value('features', features)
        l.add_value('front', front)
        l.add_value('wlan', wlan)
        l.add_value('bluetooth', bluetooth)
        l.add_value('gps', gps)
        l.add_value('usb', usb)
        l.add_value('nfc', nfc)
        l.add_value('data', data)
        l.add_value('sensors', sensors)
        l.add_value('audio', audio)
        l.add_value('browser', browser)
        l.add_value('messaging', messaging)
        l.add_value('games', games)
        l.add_value('torch', torch)
        l.add_value('extra', extra)
        l.add_value('capacity', capacity)

        return l.load_item()
