import scrapy


class Weather(scrapy.Item):
    weather = scrapy.Field()


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
