from scrapy_splash import SplashRequest

import scrapy
from missing_child.items import MissingChildItem


class ItemSpider(scrapy.Spider):
    name = 'missing_child_spider'
    allowed_domains = ['bbs.baobeihuijia.com']
    base_url = 'http://bbs.baobeihuijia.com/'
    table_xpath = '//tbody[contains(@id, "normalthread")]/tr/th/a[3]/@href'
    number_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[2]'
    sex_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[4]'
    birth_date_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[5]'
    missing_date_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[7]'
    province_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[8]'
    missing_place_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[9]'
    police_call_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[11]'
    dna_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[12]'

    def start_requests(self):
        for index in range(1, 599):
            self.logger.info('***Start for %d page, left %d page.', index, 598 - index)
            yield SplashRequest(self.base_url + 'forum-191-{0:d}.html'.format(index),
                                self.parse_urls_in_table,
                                args={'wait': 10}, )

    def parse_urls_in_table(self, response):
        for url in response.xpath(self.table_xpath).extract():
            self.logger.info('******Start item url: %s', url)
            yield SplashRequest(self.base_url + url,
                                self.parse_item_in_list,
                                args={'wait': 8}, )

    def parse_item_in_list(self, response):
        missing_child_item = MissingChildItem()

        missing_child_item['number'] = response.xpath(self.number_xpath).extract()
        missing_child_item['sex'] = response.xpath(self.sex_xpath).extract()
        missing_child_item['birth_date'] = response.xpath(self.birth_date_xpath).extract()
        missing_child_item['missing_date'] = response.xpath(self.missing_date_xpath).extract()
        missing_child_item['province'] = response.xpath(self.province_xpath).extract()
        missing_child_item['missing_place'] = response.xpath(self.missing_place_xpath).extract()
        missing_child_item['police_call'] = response.xpath(self.police_call_xpath).extract()
        missing_child_item['dna'] = response.xpath(self.dna_xpath).extract()
        missing_child_item['url'] = response.url

        yield missing_child_item
