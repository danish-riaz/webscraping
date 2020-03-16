# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.http import FormRequest
import math


class CoursesSpider(Spider):
    name = 'courses'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subject/cs']

    def __init__(self, subject=None):
        self.subject = subject
        self.page = 0
    # def parse(self, response):
    #     if self.subject:
    #         url = response.xpath(
    #             '//a[contains(@title, "' + self.subject + '")]/@href').extract_first()
    #         abs_url = 'https://www.classcentral.com' + url
    #         yield Request(abs_url, callback=self.get_data, meta = {'subject' : url})
    #     else:
    #         subjects = response.xpath(
    #             '//a[@class="border-box align-middle color-charcoal hover-no-underline"]/@href').extract()
    #         subjects = set(subjects)
    #         for subject in subjects:
    #             url = 'https://www.classcentral.com' + subject
    #             yield Request(url, callback=self.get_data)

    def parse(self, response):

        div = response.xpath(
            '//tr[@class="row nowrap vert-align-middle padding-vert-small border-bottom border-gray-light"]')

        title = div.xpath('.//td[2]/a/@title').extract()
        url = div.xpath('.//td[2]/a/@href').extract()
        category = response.xpath(
            '//h1[@class="head-1"]/text()').extract_first()
        rating = response.xpath(
            '//td[@class="hide-on-hover fill-space relative"]/@data-timestamp').extract()

        course_count = response.xpath(
            '//h2[@class="text-1"]/text()').re('[0-9]')
        course_count = int(''.join(course_count))

        for a, b, c in zip(title, url, rating):
            yield{'Title': a,
                  'Url': ('https://www.classcentral.com' + b),
                  'Rating': c,
                  'Subject': category
                  }

        # load_more = response.xpath(
        #     '//button[@class="btn-blue-outline btn-large margin-top-medium text-center"]/span[1]/text()').extract_first()
        # while True:
        #     if load_more:
        for page in range(2, (math.ceil(course_count / 50))):
            try:
                next_url = 'https://www.classcentral.com/subject/cs?page=%s' % str(
                    page + 1)
                yield Request(next_url, callback=self.parse)
            except:
                pass
            # else:
            #     break
        #     self.counter += 1
        #     joiner = '?page=' + str(self.counter)
        #     url_subject = response.meta.get('subject')
        #     url = 'https://www.classcentral.com' + str(url_subject) + joiner
        #     yield Request(url, callback=self.get_data, meta={'subject': url_subject})
        # else:

        #     self.counter = 0
