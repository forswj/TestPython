# coding:utf-8
'''
Created on 2016年10月8日

@author: Administrator
'''
import requests
import re
import os

url = r'http://jandan.net/ooxx'
dirpath = r'F:\img\meizi'

html = requests.get(url).text


regex = r'src="(.*?\.jpg)"'
pat = re.compile(regex)
urls = re.findall(pat, html)

if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

index = 1
for url in urls:
    print("下载中:", url)
    try:
        res = requests.get(url)
        if str(res.status_code)[0] == "4":
            print("未下载成功：", url)
            continue
    except Exception as e:
        print("未下载成功：", url)
    filename = os.path.join(dirpath, str(index) + ".jpg")
    with open(filename, 'wb') as f:
        f.write(res.content)
        index += 1

print("下载结束，一共 %s 张图片" % index)