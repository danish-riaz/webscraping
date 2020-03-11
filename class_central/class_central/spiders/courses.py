# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class CoursesSpider(Spider):
    name = 'courses'
    allowed_domains = ['classcentral.com/subjects']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            url = response.xpath(
                '//a[contains(@title, "+subject+")]/@href').get()
            url = 'https://www.classcentral.com' + url
            yield Request(url, callback=self.get_data)
        else:
            print("False")

    def get_data():
        pass
