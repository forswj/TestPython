# coding:utf-8
'''
Created on 2016年10月11日

@author: Administrator
'''
from urllib import request

try:
    request.urlopen("http://www.baidu.com", timeout=2)
    print("网络连接正常")
except request.URLError:
    print("网络无法连接")