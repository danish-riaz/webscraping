# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AmazonBooksPipeline(object):
    def process_item(self, item, spider):
        author = item['author']
        author = ''.join(author)
        author = author.replace(",", "")
        author = author.replace("by", "")
        item['author'] = author
        return item
