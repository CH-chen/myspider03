# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#同时爬取三个网站，怎么区分,加键判断，也可获取spider.name来判断
# 定义一个多判断

# #1.加键判断
# class Myspider03Pipeline(object):
#     def process_item(self, item, spider):
#         if item["come_from"] == 'jingdong':
#             pass
#         elif item["come_from"] == 'chouti':
#             pass
#         else:
#             pass
#         return item
#
#
# #也可以定义多个判断
# class Myspider03Pipeline2(object):
#     def process_item(self, item, spider):
#         if item["come_from"] == 'jingdong':
#             pass
#         return item
#
# class Myspider03Pipeline3(object):
#     def process_item(self, item, spider):
#
#         if item["come_from"] == 'chouti':
#             pass
#
#         return item

#2.spider.name，通过爬虫的名字来判断

import logging

logger = logging.getLogger(__name__)
class Myspider03Pipeline4(object):
    def process_item(self, item, spider): #item就是前面yieldtiem
        #spilder就是爬虫项目的类如：class Itcast1Spider(scrapy.Spider):
        #可以通过spilder.xxx获取name,allowed_domains,start_urls
        if spider.name == "itcast1": #获取类的名字判断
            logger.warning('=========')
            print(item)

        return item