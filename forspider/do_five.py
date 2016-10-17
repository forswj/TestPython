# coding:utf-8
'''
Created on 2016年10月14日

@author: Administrator
'''
import requests
import os
import re

#目录
def do_mkdir(dirth):
    if not os.path.isdir(dirth):
        os.mkdir(dirth)
        print("不存在该目录")
    else:
        print("已存在该目录，可存储图片")
        
#获取url
def get_html(url):
    html = requests.get(url).text
    return html

#爬取页面图片
def get_image(html, dirth):
    index = 1
    urls = re.findall(r' src="(.*?\.jpg)"', html)
    for url in urls:
        print("下载中：", url)
        try:
            res = requests.get(url)
            #判断报错
            if str(res.status_code)[0] == "4":
                print("下载失败：", url)
                continue
        except Exception as e:
            print("下载失败，", url)
    
        filename = os.path.join(dirth, str(index) +".jpg")
    
        with open(filename, 'wb') as f:
            f.write(res.content)
            index += 1
    print("下载结束，共下载%s张图片" %index)
    
if __name__ == '__main__':
    dirth = r'F:\222222'
    do_mkdir(dirth)
    url = r'http://www.hm5988.com'
    html = get_html(url)
    get_image(html, dirth) 