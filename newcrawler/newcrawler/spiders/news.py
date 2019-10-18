# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = []
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
