# coding:utf-8
'''
Created on 2016年10月8日

@author: Administrator
'''
from scrapy.pipelines.images import ImagesPipeline

from scrapy import Request
from scrapy.exceptions import DropItem

class PicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['pic_url']:
            yield Request(image_url)
            
    def item_completed(self, results, item, info):
        iamge_paths = [x['path'] for ok,x in results if ok]
        if not iamge_paths:
            raise DropItem("图片未下载好 %s" %iamge_paths)