# -*- coding: utf-8 -*-


import scrapy


class AllDataItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class AllClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class MouthClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class WeekClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class DayClickItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class AllRecommendItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class MouthRecommendItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class WeekRecommendItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class DayRecommendItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()


class AllCollectItem(scrapy.Item):

    name = scrapy.Field()
    author = scrapy.Field()
    count = scrapy.Field()
