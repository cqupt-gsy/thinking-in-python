import scrapy

from scrapy_splash import SplashRequest
from missing_child.items import MissingChildItem
from missing_child.spiders.spike import loadJsonDataForKey


class ItemSpider(scrapy.Spider):
    name = 'item_spider'
    allowed_domains = ['bbs.baobeihuijia.com']

    number_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[2]'
    sex_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[4]'
    birth_date_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[5]'
    missing_date_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[7]'
    province_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[8]'
    missing_place_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[9]'
    police_call_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[11]'
    dna_xpath = '//tbody/tr/td[contains(@id, "postmessage")]/ul/li[12]'

    def start_requests(self):
        for item_page in loadJsonDataForKey(key='itemLink'):
            self.logger.info('***Start for item page %s.', item_page)
            yield SplashRequest(item_page,
                                self.parse_item,
                                args={'wait': 8}, )

    def parse_item(self, response):
        missing_child_item = MissingChildItem()
        number = response.xpath(self.number_xpath).extract()
        sex = response.xpath(self.sex_xpath).extract()
        birth_date = response.xpath(self.birth_date_xpath).extract()
        missing_date = response.xpath(self.missing_date_xpath).extract()
        province = response.xpath(self.province_xpath).extract()
        missing_place = response.xpath(self.missing_place_xpath).extract()
        police_call = response.xpath(self.police_call_xpath).extract()
        dna = response.xpath(self.dna_xpath).extract()
        if (number is None or len(number) == 0) and (sex is None or len(sex) == 0) and (
                        birth_date is None or len(birth_date) == 0) and (
                missing_date is None or len(missing_date) == 0) and (
                        province is None or len(province) == 0) and (
                missing_place is None or len(missing_place) == 0) and (
                        police_call is None or len(police_call) == 0) and (dna is None or len(dna) == 0):
            missing_child_item['missingPage'] = response.url
        else:
            missing_child_item['number'] = number
            missing_child_item['sex'] = sex
            missing_child_item['birth_date'] = birth_date
            missing_child_item['missing_date'] = missing_date
            missing_child_item['province'] = province
            missing_child_item['missing_place'] = missing_place
            missing_child_item['police_call'] = police_call
            missing_child_item['dna'] = dna
        yield missing_child_item
