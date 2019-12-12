# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sqlite3
from Crawler.items import SteamItem, NewsItem

class CrawlerPipeline(object):
    def __init__(self, sql3_file):
        self.sql3_file = sql3_file

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sql3_file = os.path.join(os.path.dirname(os.path.abspath('.')), 'db.sqlite3')
        )

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sql3_file)
        self.c = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, SteamItem):
            if not self.c.execute("select userurl from UserStates where userurl = '" + item['userurl'] + "'").fetchall():
                sql = "insert into UserStates (username, state, game, crawltime, userurl)"
                sql += str.format(' values ("{0}","{1}","{2}","{3}","{4}")', item['username'], item['state'],\
                                item['game'], item['crawltime'], item['userurl'])
                self.c.execute(sql)
        elif isinstance(item, NewsItem):
            if not self.c.execute("select title from BcNews where title = '" + item['title'] + "'").fetchall():
                sql = "insert into BcNews (title, date, author, content, newsurl)"
                sql += str.format(' values ("{0}","{1}","{2}","{3}","{4}")', item['title'], item['date'],\
                                item['author'], item['content'], item['newsurl'])
                self.c.execute(sql)
        self.conn.commit()
        return item
