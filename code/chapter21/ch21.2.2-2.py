# coding=utf-8
# 代码文件：chapter21/ch21.2.2-2.py

"""获得动态数据"""
import re
import urllib.request

url = 'http://q.stock.sohu.com/hisHq?code=cn_600519&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.8115656498417958'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode('gbk')
    print(htmlstr)
    htmlstr = htmlstr.replace('historySearchHandler(', '')
    htmlstr = htmlstr.replace(')', '')
    print('替换后的：', htmlstr)
