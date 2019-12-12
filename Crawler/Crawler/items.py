# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamItem(scrapy.Item):
    username = scrapy.Field()
    state = scrapy.Field()
    game = scrapy.Field()
    crawltime = scrapy.Field()
    userurl = scrapy.Field()

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    newsurl = scrapy.Field()
