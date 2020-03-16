# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
import math


class CoursesSpider(Spider):
    name = 'courses'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://www.classcentral.com/subject/cs',
                  'https://www.classcentral.com/subject/business',
                  'https://www.classcentral.com/subject/humanities',
                  'https://www.classcentral.com/subject/data-science',
                  'https://www.classcentral.com/subject/personal-development',
                  'https://www.classcentral.com/subject/art-and-design',
                  'https://www.classcentral.com/subject/programming-and-software-development',
                  'https://www.classcentral.com/subject/engineering',
                  'https://www.classcentral.com/subject/health',
                  'https://www.classcentral.com/subject/maths',
                  'https://www.classcentral.com/subject/science',
                  'https://www.classcentral.com/subject/social-sciences',
                  'https://www.classcentral.com/subject/education',
                  ]

    def parse(self, response):
        self.current_sub = response.url
        self.current_sub = self.current_sub.split('/')[4]
        yield Request(response.url, callback=self.get_data)

    def get_data(self, response):
        course_count = response.xpath(
            '//h2[@class="text-1"]/text()').re('[0-9]')
        course_count = int(''.join(course_count))
        for page in range(0, (math.ceil(course_count / 50))):
            next_url = 'https://www.classcentral.com/subject/' + self.current_sub + '?page=%s' % str(
                page + 1)
            yield Request(next_url, callback=self.loop_thorugh)

    def loop_thorugh(self, response):

        div = response.xpath(
            '//tr[@class="row nowrap vert-align-middle padding-vert-small border-bottom border-gray-light"]')

        title = div.xpath('.//td[2]/a/@title').extract()
        url = div.xpath('.//td[2]/a/@href').extract()
        category = response.xpath(
            '//h1[@class="head-1"]/text()').extract_first()
        rating = response.xpath(
            '//td[@class="hide-on-hover fill-space relative"]/@data-timestamp').extract()

        for a, b, c in zip(title, url, rating):
            yield{'Title': a,
                  'Url': ('https://www.classcentral.com' + b),
                  'Rating': c,
                  'Subject': category,
                  'Global_URL': response.url
                  }
