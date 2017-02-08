# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["monex.co.jp"]
    start_urls = (
        'http://www.monex.co.jp/',
    )

    def parse(self, response):
        pass
