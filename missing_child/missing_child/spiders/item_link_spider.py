import scrapy

from scrapy_splash import SplashRequest
from missing_child.items import ItemLink


class TableLinkSpider(scrapy.Spider):
    name = 'item_link_spider'
    allowed_domains = ['bbs.baobeihuijia.com']
    base_url = 'http://bbs.baobeihuijia.com/'
    item_xpath = '//tbody[contains(@id, "normalthread")]/tr/th/a[3]/@href'

    def start_requests(self):
        for index in range(1, 599):
            self.logger.info('***Start for %d page, left %d page.', index, 598 - index)
            yield SplashRequest(self.base_url + 'forum-191-{0:d}.html'.format(index),
                                self.parse_urls_in_table,
                                args={'wait': 6}, )

    def parse_urls_in_table(self, response):
        item_links = response.xpath(self.item_xpath).extract()
        if item_links is None or len(item_links) == 0:
            self.logger.info('******Miss fetched item url: %s', response.url)
            item_link = ItemLink()
            item_link['missingPage'] = response.url
            yield item_link
        else:
            for url in item_links:
                self.logger.info('******Fetched item url: %s', url)
                item_link = ItemLink()
                item_link['itemLink'] = self.base_url + url
                yield item_link

