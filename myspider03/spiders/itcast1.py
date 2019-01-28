# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)  #__name__，log日志回显示当前py文件路径的log日志；[myspider03.spiders.itcast1]，不加__name__,显示root

class Itcast1Spider(scrapy.Spider):
    name = 'itcast1' #爬虫名称
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item = {}
            item["come_from"] = 'jingdong'
            # logging.warning(item) #可以通过 loggin输出的内容保存在本地，可以查看log日志，查看程序状态，但是这个保存在根目录，一般不用
            logger.warning(item)
            yield item #注意yield的位置，在for循环内核循环外的区别
