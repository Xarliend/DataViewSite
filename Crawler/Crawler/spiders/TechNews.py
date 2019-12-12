# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import NewsItem

class TechnewsSpider(scrapy.Spider):
    name = 'TechNews'
    allowed_domains = ['technews.tw']
    start_urls = ['https://technews.tw/category/fintech/']

    def parse(self, response):
        raw = response.xpath('//h1[@class="entry-title"]/a').getall()
        newstitles = [(t.split('"')[3], t.split('"')[1]) for t in raw ]
        for title in newstitles:
            if '區塊鏈' in title[0]:
                yield scrapy.Request(title[1], callback=self.Blockchain)

    def Blockchain(self, response):
        item = NewsItem()
        item['newsurl'] = response.url
        item['title'] = response.xpath('//h1/a/text()').get()
        item['date'] = response.css('header.entry-header').xpath('./table/tr[2]/td/span[@class="body"][2]/text()').get()
        item['author'] = response.css('header.entry-header').xpath('./table/tr[2]/td/span[@class="body"][1]/a/text()').get()
        rawcontent = response.xpath('string(//div[@class="indent"])').getall()
        item['content'] = rawcontent[0].strip()
        yield item
