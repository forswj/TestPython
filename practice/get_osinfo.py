# coding:utf-8
'''
Created on 2016年10月10日

@author: Administrator
'''

import platform as pl

profile = [
'architecture',
'linux_distribution',
'mac_ver',
'machine',
'node',
'platform',
'processor',
'python_build',
'python_compiler',
'python_version',
'release',
'system',
'uname',
'version',
]


for key in profile:
    if hasattr(pl,key):
        print(key + ": "+ str(getattr(pl,key)()))
        