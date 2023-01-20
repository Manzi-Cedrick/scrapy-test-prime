# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ListcontractsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    def parse(self, response):
        item = ListcontractsItem()
        item['file_urls'] = [response.urljoin(url) for url in response.css('img::attr(src)').getall()]
        yield item
