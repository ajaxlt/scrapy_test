import scrapy
from scrapy_test.items import ScrapyTestItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do?positionName=iOS']

    def parse(self, response):
        node = response.xpath("//tbody/tr")[::2]
        for i in range(len(node)):
            item = ScrapyTestItem()
            item['_id'] = i + 1
            item['name'] = node[i].xpath("./td[1]/a/text()").extract_first()  # 工作名
            item['work_class'] = node[i].xpath("./td[3]/text()").extract_first()  # 职位类别
            item['work_type'] = node[i].xpath("./td[4]/text()").extract_first()  # 全职？
            item['work_place'] = node[i].xpath("./td[5]/text()").extract_first()  # 工作地点
            item['date'] = node[i].xpath("./td[7]/text()").extract_first()  # 发布时间
            yield item
