# -*- coding: utf-8 -*-
# 使用gsExtractor类的示例程序
# 访问集搜客论坛，以xslt为模板提取论坛内容
# xslt保存在xslt_bbs.xml中
# 采集结果保存在result.xml中

import os
from urllib import request
import lxml
from lxml import etree
import gooseeker
from gooseeker import GsExtractor

# 访问并读取网页内容
url = "http://www.gooseeker.com/cn/forum/7"
conn = request.urlopen(url)
doc = etree.HTML(conn.read())

bbsExtra = GsExtractor()   
bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e" , "gooseeker_bbs_xslt")   # 设置xslt抓取规则
result = bbsExtra.extract(doc)   # 调用extract方法提取所需内容

# 当前目录
current_path = os.getcwd()
file_path = current_path + "/result.xml"

# 保存结果
open(file_path,"wb").write(result)