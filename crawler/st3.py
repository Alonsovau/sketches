import scrapy
import time
from urllib.request import urlopen
import os


class Weather(scrapy.Item):
    cityDate = scrapy.Field()
    week = scrapy.Field()
    img = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()


class szSpider(scrapy.Spider):
    name = 'szSpider'
    allowed_domains = ['tianqi.com']
    citys = ['suzhou', 'shanghai']
    start_urls = []
    for city in citys:
        start_urls.append('http://' + city + '.tianqi.com')

    def parse(self, response):
        subSelector = response.xpath('//div[@class="tqshow1"]')
        items = []
        for sub in subSelector:
            item = Weather()
            cityDates = ''
            for cityDate in sub.xpath('./h3//text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates
            item['week'] = sub.xpath('./p//text()').extract()[0]
            item['img'] = sub.xpath('./ul/li[1]/img/@src').extract()[0]
            temps = ''
            for temp in sub.xpath('./ul/li[2]//text()').extract():
                temps += temp
            item['temperature'] = temps
            item['weather'] = sub.xpath('./ul/li[3]//text()').extract()[0]
            items.append(item)
        return items


def process_item(item):
    today = time.strftime('%Y-%m-%d', time.localtime())
    fileName = today + '.txt'
    with open(fileName, 'a') as f:
        f.write(item['cityDate'].encode('utf8') + '\t')
        f.write(item['week'].encode('utf8') + '\t')
        imgName = os.path.basename(item['img'])
        f.write(imgName + '\t')
        if os.path.exists(imgName):
            pass
        else:
            with open(imgName, 'wb') as f:
                response = urlopen(item['img'])
                f.write(response.read())
        time.sleep(1)


if __name__ == '__main__':
    spider = szSpider()
    items = spider.parse(scrapy.)
    process_item(spider)