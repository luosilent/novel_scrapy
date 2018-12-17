from scrapy.spider import Spider
from novel.items import AllClickItem
from novel.items import MouthClickItem
from novel.items import WeekClickItem
from novel.items import DayClickItem
import re


class AllNovelSpider(Spider):
    name = 'all_click_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u1/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 6, 1)]

    def parse(self, response):
        item = AllClickItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 总点击

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['click'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class MouthNovelSpider(Spider):
    name = 'mouth_click_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u6/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 6, 1)]

    def parse(self, response):
        item = MouthClickItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 月点击

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['click'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class WeekNovelSpider(Spider):
    name = 'week_click_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u9/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 6, 1)]

    def parse(self, response):
        item = WeekClickItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 周点击

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['click'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class DayNovelSpider(Spider):
    name = 'day_click_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u12/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 6, 1)]

    def parse(self, response):
        item = DayClickItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 月点击

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['click'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item
