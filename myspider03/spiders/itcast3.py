# -*- coding: utf-8 -*-
import scrapy


class Itcast3Spider(scrapy.Spider):
    name = 'itcast3'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        item = {}
        item["come_from"] = 'qichezhjia'
