# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import urllib.request

class ScrapyTestPipeline(object):

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mydb = self.client['test']
        self.mycol = self.mydb['job']
    def process_item(self, item, spider):
        item = dict(item)
        self.mycol.insert_one(item)
        return item
    def __del__(self):
        self.client.close()


class ScrapyDownloadPipeline(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.mydb = self.client['test']
        self.mycol = self.mydb['job']

    def process_item(self, item, spider):
        item = dict(item)
        self.mycol.insert_one(item)
        return item

    def __del__(self):
        self.client.close()