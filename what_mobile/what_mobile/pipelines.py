# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import re


def clean_spaces(item, spider):
    gen_dic = {'\xa0': ''}
    for key, value in item.items():
        if len(value) != 0:
            local_item = item[key]
            for k, v in gen_dic.items():
                local_item = [i.replace(k, v) for i in local_item]
                local_item = ''.join(local_item)
                local_item = re.sub(' +', ' ', local_item)
                item[key] = local_item


class WhatMobilePipeline(object):
    def process_item(self, item, spider):
        price = item['price_pkr']
        price_flag = False
        # Seting price
        dic_price = {' ': '', '\n': '', 'R': '',
                     'S': '', '.': '', ',': '', 'r': '', 's': ''}
        for k, v in dic_price.items():
            price = [i.replace(k, v) for i in price]
            price = ''.join(price)
        try:
            if(int(price) < 300):
                price_flag = True
        except:
            pass
        # checking item should be droped or contiue
        if(price_flag):
            clean_spaces(item, spider)
            return item
        else:
            raise DropItem("Missing price in %s" % item)
        # RAM
        # flag_1 = False
        # flag_2 = False
        # flag_3 = False
        # if len(item['built_in']) != 0:
        #     built_in = item['built_in']
        #     built_in = built_in[0][built_in[0].find(","):]
        #     dic = {' ': '', '\xa0': '', ',': ''}
        #     for k, v in dic.items():
        #         built_in = built_in.replace(k, v)
        #     built_in = built_in[(built_in.find("G") - 1):built_in.find("G")]
        #     built_in = ''.join(built_in)
        #     if len(built_in) != 0:
        #         flag_1 = True
        # # PRICE
        # if len(item['price_pkr']) != 0:
        #     price_pkr = item['price_pkr']
        #     dic_price = {' ': '', '\n': '', 'R': '',
        #                  'S': '', '.': '', ',': '', 'r': '', 's': ''}
        #     for k, v in dic_price.items():
        #         price_pkr = [i.replace(k, v) for i in price_pkr]
        #         # price_pkr = price_pkr.replace(k, v)
        #     price_pkr = ''.join(price_pkr)
        #     if len(price_pkr) != 0 and price_pkr == 'Comingoon':
        #         flag_2 = True

        # if len(item['main']) != 0:
        #     main = item['main']
        #     main = main[0][(main[0].find("M") - 3):(main[0].find("M") - 1)]
        #     main = ''.join(main)
        #     if len(main) != 0:
        #         flag_3 = True

        # gen_dic = {'\n': '', '\xa0': ''}
        # for key in item.keys():
        #     local_item = item[key]
        #     for k, v in gen_dic.items():
        #         local_item = [i.replace(k, v) for i in local_item]
        #         local_item = ''.join(local_item)
        #         local_item = re.sub(' +', ' ', local_item)
        #         item[key] = local_item
        # return item
        # if (flag_1 and flag_2 and flag_3):
        #     if ((int(built_in) >= 4) and (int(price_pkr) <= 30000) and (int(main) < 20)):
        #         gen_dic = {'\n': '', '\xa0': ''}
        #         for key, value in item.items():
        #             if len(value) != 0:
        #                 local_item = item[key]
        #                 for k, v in gen_dic.items():
        #                     local_item = [i.replace(k, v) for i in local_item]
        #                     local_item = ''.join(local_item)
        #                     local_item = re.sub(' +', ' ', local_item)
        #                     item[key] = local_item
        #                     return item
        # gen_dic = {'\n': '', '\xa0': ''}
        # for key, value in item.items():
        #     if len(value) != 0:
        #         local_item = item[key]
        #         for k, v in gen_dic.items():
        #             local_item = [i.replace(k, v) for i in local_item]
        #             local_item = ''.join(local_item)
        #             local_item = re.sub(' +', ' ', local_item)
        #             item[key] = local_item
        #             return item
        # else:
        #     # gen_dic = {'\n': '', '\xa0': ''}
        #     # for key in item.keys():
        #     #     local_item = item[key]
        #     #     for k, v in gen_dic.items():
        #     #         local_item = [i.replace(k, v) for i in local_item]
        #     #         local_item = ''.join(local_item)
        #     #         local_item = re.sub(' +', ' ', local_item)
        #     #         item[key] = local_item
        #     # return item

        #     gen_dic = {'\n': '', '\xa0': ''}
        #     for key, value in item.items():
        #         if len(value) != 0:
        #             local_item = item[key]
        #             for k, v in gen_dic.items():
        #                 local_item = [i.replace(k, v) for i in local_item]
        #                 local_item = ''.join(local_item)
        #                 local_item = re.sub(' +', ' ', local_item)
        #                 item[key] = local_item
        #                 return item
        # raise DropItem("Missing price in %s" % item)
