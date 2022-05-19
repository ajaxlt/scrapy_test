# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from scrapy.http import HtmlResponse
from selenium import webdriver
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        url = request.url
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(15)
        data = driver.page_source

        driver.close()

        res = HtmlResponse(url=url, body=data, encoding='utf-8', request=request)
        return res
    def process_response(self, request, response, spider):
        print('1')
        return response