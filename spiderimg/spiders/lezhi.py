# -*- coding: utf-8 -*-
import scrapy
import json
from spiderimg.items import SpiderimgItem
class LezhiSpider(scrapy.Spider):
    name = 'imagespider'
    allowed_domains = ['douyucdn.cn']
    baseURL="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=1&&offset="
    offset=0
    start_urls = [baseURL+str(offset)]

    def parse(self, response):
        data_list=json.loads(response.body)['data']
        if not len(data_list):
            return
        item=SpiderimgItem()
        for data in data_list:
            item['nickname']=data['nickname']
            item['imagelink']=data['vertical_src']
            yield item

        self.offset +=1
        yield scrapy.Request(self.baseURL+str(self.offset),callback=self.parse)