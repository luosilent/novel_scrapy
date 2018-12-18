#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 9:16
# @Author  : luoSilent
# @File    : ALLData.py
# @Software: PyCharm

from novel.items import AllDataItem
from scrapy.spider import Spider
from novel.items import AllClickItem
from novel.items import MouthClickItem
from novel.items import WeekClickItem
from novel.items import DayClickItem
from novel.items import AllRecommendItem
from novel.items import MouthRecommendItem
from novel.items import WeekRecommendItem
from novel.items import DayRecommendItem
from novel.items import AllCollectItem
import re


class AllNovelSpider(Spider):
    name = 'all_data_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }
    kind = (1, 2, 4, 6, 7, 9, 10, 12, 13)
    start_urls = [
        'http://book.zongheng.com/store/c0/c0/b0/u%d/p1/v9/s9/t0/u0/i0/ALL.html' % n for n in kind

    ]

    def parse(self, response):
        if re.search('/u1/', response.url):
            item = AllClickItem()
        elif re.search('/u6/', response.url):
            item = MouthClickItem()
        elif re.search('/u9/', response.url):
            item = WeekClickItem()
        elif re.search('/u12/', response.url):
            item = DayClickItem()
        elif re.search('/u2/', response.url):
            item = AllRecommendItem()
        elif re.search('/u7/', response.url):
            item = MouthRecommendItem()
        elif re.search('/u10/', response.url):
            item = WeekRecommendItem()
        elif re.search('/u13/', response.url):
            item = DayRecommendItem()
        elif re.search('/u4/', response.url):
            item = AllCollectItem()
        else:
            item = AllDataItem()

        novels = response.xpath('//ul[@class="main_con"]/li')

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item
