# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import SteamItem
from datetime import datetime


class UserstatesSpider(scrapy.Spider):
    name = 'userstates'
    allowed_domains = ['steamcommunity.com']
    start_urls = ['https://steamcommunity.com/groups/pttcc/members/']

    def parse(self, response):
        pages = 12412//51+1
        for p in range(1, pages+1):
            yield scrapy.Request('https://steamcommunity.com/groups/pttcc/members/?p='+str(p), callback=self.GetState)

    def GetState(self, response):
        ustates = response.xpath('//div[@id="memberList"]').css('div.member_block_content')
        for s in ustates:
            item = SteamItem()
            item['crawltime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['username'] = s.css('a::text').get()
            item['state'] = s.css('div.friendSmallText::text').get()
            if 'In-Game' in item['state']:
                item['game'] = s.css('div.friendSmallText::text').getall()[1]
            else:
                item['game'] = ''
            item['userurl'] = s.css('a::attr(href)').get()
            yield item
