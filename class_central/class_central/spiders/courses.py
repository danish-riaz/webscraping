# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class CoursesSpider(Spider):
    name = 'courses'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject
        self.counter = 1

    def parse(self, response):
        if self.subject:
            url = response.xpath(
                '//a[contains(@title, "' + self.subject + '")]/@href').extract_first()
            url = 'https://www.classcentral.com' + url
            yield Request(url, callback=self.get_data, dont_filter=True)
        else:
            subjects = response.xpath(
                '//a[@class="border-box align-middle color-charcoal hover-no-underline"]/span[1]/text()').extract()
            subjects = set(subjects)
            for subject in subjects:
                url = response.xpath(
                    '//a[contains(@title, "' + subject + '")]/@href').extract_first()
                url = 'https://www.classcentral.com' + url
                self.logger.info(
                    "############################# INSIDE SUBJECT ############################")
                self.subject = subject
                yield Request(url, callback=self.get_data, dont_filter=True)
                self.subject = subject

    def get_data(self, response):
        self.logger.info(
            "############################# GETTING DATA ############################")
        div = response.xpath(
            '//tr[@class="row nowrap vert-align-middle padding-vert-small border-bottom border-gray-light"]')

        title = div.xpath('.//td[2]/a/@title').extract()
        url = div.xpath('.//td[2]/a/@href').extract()
        rating = response.xpath(
            '//td[@class="hide-on-hover fill-space relative"]/@data-timestamp').extract()
        for a, b, c in zip(title, url, rating):
            yield{'Title': a,
                  'Url': ('https://www.classcentral.com' + b),
                  'Rating': c,
                  'Subject': self.subject
                  }
        # load_more = response.xpath(
        #     '//button[@class="btn-blue-outline btn-large margin-top-medium text-center"]/span[1]/text()').extract_first()
        # if load_more:
        #     self.counter += 1
        #     url = 'https://www.classcentral.com/subject/' + self.subject + '?page=' + \
        #         str(self.counter)
        #     self.logger.info(
        #         "############################# LOAD MORE ############################")
        #     yield Request(url, callback=self.get_data)
