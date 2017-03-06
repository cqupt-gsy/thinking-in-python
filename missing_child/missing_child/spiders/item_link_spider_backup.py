import json
import scrapy

from scrapy_splash import SplashRequest
from missing_child.items import ItemLink
from missing_child.spiders.spike import loadJsonDataForKey


class TableLinkSpiderBackup(scrapy.Spider):
    name = 'item_link_spider_backup'
    allowed_domains = ['bbs.baobeihuijia.com']
    base_url = 'http://bbs.baobeihuijia.com/'
    table_xpath = '//tbody[contains(@id, "normalthread")]/tr/th/a[3]/@href'

    def start_requests(self):
        for missing_page in loadJsonDataForKey(backup='item_link_backup.json'):
            self.logger.info('***Start missing page %s.', missing_page)
            yield SplashRequest(missing_page,
                                self.parse_urls_in_table,
                                args={'wait': 6}, )

    def parse_urls_in_table(self, response):
        item_links = response.xpath(self.table_xpath).extract()
        if item_links is None or len(item_links) == 0:
            self.logger.info('******Miss fetched item url: %s', response.url)
            item_link_item = ItemLink()
            item_link_item['missingPage'] = response.url
            yield item_link_item
        else:
            for url in item_links:
                self.logger.info('******Fetched item url: %s', url)
                item_link_item = ItemLink()
                item_link_item['itemLink'] = self.base_url + url
                yield item_link_item
