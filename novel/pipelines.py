# -*- coding: utf-8 -*-

from novel.items import AllClickItem
from novel.items import MouthClickItem
from novel.items import WeekClickItem
from novel.items import DayClickItem
from novel.items import AllRecommendItem
from novel.items import MouthRecommendItem
from novel.items import WeekRecommendItem
from novel.items import DayRecommendItem
from novel.items import AllCollectItem

import pymysql


class NovelPipeline(object):

    def __init__(self):

        self.connect = pymysql.connect(

            host='127.0.0.1',
            db='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
            use_unicode=True)

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        if isinstance(item, AllClickItem):
            sql = 'insert into scrapy.novel_a_click(name,author,click) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, MouthClickItem):
            sql = 'insert into scrapy.novel_m_click(name,author,click) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, WeekClickItem):
            sql = 'insert into scrapy.novel_w_click(name,author,click) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, DayClickItem):
            sql = 'insert into scrapy.novel_d_click(name,author,click) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, AllRecommendItem):
            sql = 'insert into scrapy.novel_a_recommend(name,author,recommend) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, MouthRecommendItem):
            sql = 'insert into scrapy.novel_m_recommend(name,author,recommend) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, WeekRecommendItem):
            sql = 'insert into scrapy.novel_w_recommend(name,author,recommend) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, DayRecommendItem):
            sql = 'insert into scrapy.novel_d_recommend(name,author,recommend) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        elif isinstance(item, AllCollectItem):
            sql = 'insert into scrapy.novel_a_collect(name,author,collect) values (%s,%s,%s)'
            self.cursor.execute(sql, (item['name'], item['author'], item['count']))
            self.connect.commit()

        return item
