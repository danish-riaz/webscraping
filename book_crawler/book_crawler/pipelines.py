# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import urllib.request


def dwnlaod_image(url, path, name):
    dic = {':': '',
           ',': '',
           ' ': '',
           '"': '',
           "'": ''}
    for k, v in dic.items():
        name = name.replace(k, v)
    full_path = path + name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


# def clear_folder(path):
#     filelist = [f for f in os.listdir(path)]
#     if len(filelist) != 0:
#         for f in filelist:
#             os.remove(os.path.join(path, f))


class BookCrawlerPipeline(object):
    def process_item(self, item, spider):
        path = '/media/dani/Hard Disk/Danish/Paractice/webscraping/book_crawler/Images/'
        if float(item['price'][0][1:]) < 25:
            # clear_folder(path)
            dwnlaod_image(
                item['image_urls'][0], path, item['h1'][0])
            return item
        else:
            raise DropItem("Missing price in %s" % item)
