# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import urllib.request
import shutil


def dwnlaod_image(url, path, name):
    dic = {':': '',
           ',': '',
           ' ': '',
           '"': '',
           "'": ''}
    for k, v in dic.items():
        name = name.replace(k, v)
    shutil.rmtree(path+'/img')
    full_path = path + name + '.jpg'
    urllib.request.urlretrieve(url, full_path)
    # r = requests.get(url, allow_redirects=True)
    # open(full_path, 'wb').write(r.content)


class BookCrawlerPipeline(object):
    def process_item(self, item, spider):
        if float(item['price'][0][1:]) > 25:
            dwnlaod_image(
                item['image_urls'][0], '/media/dani/Hard Disk/Danish/Paractice/webscraping/book_crawler/Images/', item['h1'][0])
            return item
        else:
            raise DropItem("Missing price in %s" % item)
