# -*- coding: utf-8 -*-


import scrapy


class AllClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    click = scrapy.Field()


class MouthClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    click = scrapy.Field()


class WeekClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    click = scrapy.Field()


class DayClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    click = scrapy.Field()
