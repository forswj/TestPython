# coding:utf-8
'''
Created on 2016年10月8日

@author: Administrator
'''
from scrapy.spiders import Spider
from scrapy.selector import Selector

from testScrapy.items import AiriPicItem

class pic_spider(Spider):
    name = 'pic_spider'
    start_urls = [
         'http://jandan.net/ooxx'
    ]
    
    def parse(self, response):
        sel = Selector(response)
        
        image_url = sel.xpath("//div[@id='comment-3275154']/div[1]/div/div[2]/p/img[1]").extract()
        print('the urls:/n')
        print(image_url)
        print('/n')
        
        item = AiriPicItem()
        item['pic_url'] = image_url
        
        yield item
    