# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['mtime.com']
    start_urls = ['http://mtime.com/']

    def parse(self, response):
        pass
