# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE as image_url
class SpiderimgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        imagelink=item['imagelink']
        yield scrapy.Request(imagelink)

    def item_completed(self, results, item, info):
        imagepath=[x["path"] for ok,x in results if ok]
        os.rename(image_url+imagepath[0],image_url+item["nickname"]+".jpg")
        return item


