import scrapy

from scrapy_splash import SplashRequest
from missing_child.items import MissingChildItem
from missing_child.spiders.json_helper import loadJsonDataForKey


class ItemSpider(scrapy.Spider):
    name = 'item_spider'
    allowed_domains = ['bbs.baobeihuijia.com']

    ul_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul'

    def start_requests(self):
        for item_page in loadJsonDataForKey(key='itemLink'):
            self.logger.info('***Start for item page %s.', item_page)
            yield SplashRequest(item_page,
                                self.parse_item,
                                args={'wait': 10})

    def parse_item(self, response):
        missing_child_item = MissingChildItem()
        content = response.xpath(self.ul_xpath).extract()
        if content is None or len(content) == 0:
            self.logger.info('***Missing for item page %s.', response.url)
            missing_child_item['missingPage'] = response.url
        else:
            missing_child_item['content'] = content
        yield missing_child_item
