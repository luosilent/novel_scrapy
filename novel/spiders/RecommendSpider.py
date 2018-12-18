from scrapy.spider import Spider
from novel.items import AllRecommendItem
from novel.items import MouthRecommendItem
from novel.items import WeekRecommendItem
from novel.items import DayRecommendItem
import re


class AllNovelSpider(Spider):
    name = 'all_rem_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u2/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 10, 1)]

    def parse(self, response):
        item = AllRecommendItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 总推荐

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class MouthNovelSpider(Spider):
    name = 'mouth_rem_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u7/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 10, 1)]

    def parse(self, response):
        item = MouthRecommendItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 月推荐

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class WeekNovelSpider(Spider):
    name = 'week_rem_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u10/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 10, 1)]

    def parse(self, response):
        item = WeekRecommendItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 周推荐

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item


class DayNovelSpider(Spider):
    name = 'day_rem_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u13/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 10, 1)]

    def parse(self, response):
        item = DayRecommendItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 日推荐

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item
