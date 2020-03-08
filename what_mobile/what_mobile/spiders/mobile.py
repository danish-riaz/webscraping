# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


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
        mobile_name = response.xpath(
            '//h1[@class="hdng3"]/text()').extract_first()
        price_pkr = response.xpath('//*[@class="hdng"]/text()')[0].extract()
        price_usd = response.xpath('//*[@class="hdng"]/text()')[1].extract()
        rating = response.xpath(
            '//*[contains(@class, "rateit")]/@data-rateit-value')[0].extract()
        os = first_element(response, "OS")
        ui = after_first_element(response, "UI")
        dimensions = after_first_element(response, "Dimensions")

        yield{'Mobile_Name': mobile_name,
              'PRICE PKR': price_pkr,
              'PRICE USD': price_usd}
