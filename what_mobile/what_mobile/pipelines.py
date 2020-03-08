# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class WhatMobilePipeline(object):
    def process_item(self, item, spider):
        # RAM
        built_in = item['built_in']
        built_in = built_in[0][built_in[0].find(","):]
        dic = {' ': '', '\xa0': '', ',': ''}
        for k, v in dic.items():
            built_in = built_in.replace(k, v)
        built_in = built_in[(built_in.find("G") - 1):built_in.find("G")]
        # PRICE
        price_pkr = item['price_pkr']
        dic_price = {' ': '', '\n': '', 'R': '',
                     'S': '', '.': '', ',': '', 'r': '', 's': ''}
        for k, v in dic_price.items():
            price_pkr = price_pkr.replace(k, v)

        main = item['main']
        main = main[0][(main[0].find("M") - 3):(main[0].find("M") - 1)]

        if (int(built_in) >= 4 and int(price_pkr) <= 30000 and int(main) > 20):
            return item

        else:
            raise DropItem("Missing price in %s" % item)
