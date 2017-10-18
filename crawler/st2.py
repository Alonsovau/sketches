import scrapy
import time


class TodayMovieItem(scrapy.Item):
    movieName = scrapy.Field()


class MovieSpider(scrapy.Spider):
    name = 'Movie Spider'
    allowed_domains = ['jycinema.com']
    start_urls = ('http://www.jycinema.com/browing/Cinemas/Details/1029',)

    def parse(self, response):
        subSelector = response.xpath('//div[@class="film-header"]')
        items = []
        for sub in subSelector:
            item = TodayMovieItem()
            item['movieName'] = sub.xpath('./a/h3/text()').extract()
            items.append(items)
            return items


class TodaymoviePipeline():
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        fileName = 'wuHan' + now + '.txt'
        with open(fileName, 'a') as f:
            f.write(item['movieName'][0].encode('utf8') + '\n\n')
        return item
