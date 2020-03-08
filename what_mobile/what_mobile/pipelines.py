# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re


class WhatMobilePipeline(object):
    def process_item(self, item, spider):
        # RAM
        built_in = item['built_in']
        built_in = built_in[0][built_in[0].find(","):]
        dic = {' ': '', '\xa0': '', ',': ''}
        for k, v in dic.items():
            built_in = built_in.replace(k, v)
        built_in = built_in[(built_in.find("G") - 1):built_in.find("G")]
        built_in = ''.join(built_in)
        # PRICE
        price_pkr = item['price_pkr']
        dic_price = {' ': '', '\n': '', 'R': '',
                     'S': '', '.': '', ',': '', 'r': '', 's': ''}
        for k, v in dic_price.items():
            price_pkr = [i.replace(k, v) for i in price_pkr]
            # price_pkr = price_pkr.replace(k, v)
        price_pkr = ''.join(price_pkr)
        main = item['main']
        main = main[0][(main[0].find("M") - 3):(main[0].find("M") - 1)]
        main = ''.join(main)

        gen_dic = {'\n': '', '\xa0': ''}
        for key in item.keys():
            local_item = item[key]
            for k, v in gen_dic.items():
                local_item = [i.replace(k, v) for i in local_item]
                local_item = ''.join(local_item)
                local_item = re.sub(' +', ' ', local_item)
                item[key] = local_item
        return item

        # if ((int(built_in) >= 4) and (int(price_pkr) <= 30000) and (int(main) < 20)):
        #     gen_dic = {'\n': '', '\xa0': ''}
        #     for key in item.keys():
        #         local_item = item[key]
        #         for k, v in gen_dic.items():
        #             local_item = [i.replace(k, v) for i in local_item]
        #             local_item = ''.join(local_item)
        #             local_item = re.sub(' +', ' ', local_item)
        #             item[key] = local_item
        #     return item

        # else:
        # gen_dic = {'\n': '', '\xa0': ''}
        # for key in item.keys():
        #     local_item = item[key]
        #     for k, v in gen_dic.items():
        #         local_item = [i.replace(k, v) for i in local_item]
        #         local_item = ''.join(local_item)
        #         local_item = re.sub(' +', ' ', local_item)
        #         item[key] = local_item
        # return item
        # raise DropItem("Missing price in %s" % item)
