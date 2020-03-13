# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class CoursesSpider(Spider):
    name = 'courses'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            url = response.xpath(
                '//a[contains(@title, "' + self.subject + '")]/@href').extract_first()
            url = 'https://www.classcentral.com' + url
            yield Request(url, callback=self.get_data)
        else:
            print("False")

    def get_data(self, response):
        div = response.xpath(
            '//tr[@class="row nowrap vert-align-middle padding-vert-small border-bottom border-gray-light"]')

        title = div.xpath('.//td[2]/a/@title').extract()
        url = div.xpath('.//td[2]/a/@href').extract()
        rating = response.xpath(
            '//td[@class="hide-on-hover fill-space relative"]/@data-timestamp').extract()
        for a, b, c in zip(title, url, rating):
            yield{'title': a,
                  'url': ('https://www.classcentral.com' + b),
                  'rating': c
                  }
        yield Request('https://www.classcentral.com/subject/humanities?page=2', callback=self.get_data)
