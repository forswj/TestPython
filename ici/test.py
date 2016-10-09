#coding=utf8

import requests
import sys
print(sys.version)
r = requests.get('http://cuiqingcai.com')
print(type(r))

print(r.status_code)
print(r.encoding)
print(r.cookies)