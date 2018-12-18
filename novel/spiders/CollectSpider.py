from scrapy.spider import Spider
from novel.items import AllCollectItem
import re


class AllNovelSpider(Spider):
    name = 'all_collect_spider'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.143 Safari/537.36'
    }

    start_urls = ['http://book.zongheng.com/store/c0/c0/b0/u4/p%d/v9/s9/t0/u0/i0/ALL.html' % i for i in range(1, 10, 1)]

    def parse(self, response):
        item = AllCollectItem()
        novels = response.xpath('//ul[@class="main_con"]/li')  # 总收藏

        for novel in novels:
            item['name'] = novel.xpath('.//span[@class="bookname"]/a/text()').extract()[0]
            item['author'] = novel.xpath('.//span[@class="author"]/a/text()').extract()[0]
            item['count'] = re.findall(r"\d+\.?\d*", novel.xpath('.//span[@class="count"]/text()').extract()[0])

            yield item
