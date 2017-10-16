from scrapy.selector import Selector


with open('superHero.xml') as f:
    source = f.read()
    x = Selector(text=source).xpath('/*').extract()
    print(x)
    x = Selector(text=source).css('class').extract()
    print(x)
    x = Selector(text=source).css('class name').extract()
    print(x)
    x = Selector(text=source).css('[lang]').extract()
    print(x)
    x = Selector(text=source).css('[lang=en]').extract()
    print(x)
