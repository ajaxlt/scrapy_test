import scrapy
import json
from scrapy_test.items import ScrapyTestItem

class TestPostSpider(scrapy.Spider):
    name = 'test_post'
    allowed_domains = ['163.com']
    # start_urls = ['https://hr.163.com/api/hr163/position/queryPage']

    def start_requests(self):
        url = 'https://hr.163.com/api/hr163/position/queryPage'
        data = {
            "currentPage": 1, "pageSize": 20, "workType": "1",
        }
        yield scrapy.FormRequest(url=url,  body=json.dumps(data), method='POST', callback=self.parse)
    def parse(self, response):
        res = json.loads(response.text)['data']['list']
        for i in range(len(res)):
            _id = i + 1
            name = res[i]['name']
            recuit_num = res[i]['recruitNum']
            req_education = res[i]['reqEducationName']
            dep_name = res[i]['firstDepName']
            item = ScrapyTestItem(_id=_id, name=name, recuit_num=recuit_num, req_education=req_education, dep_name=dep_name)

            yield item


