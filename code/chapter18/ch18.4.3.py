# coding=utf-8
# 代码文件：chapter18/ch18.4.3.py

import urllib.request

with urllib.request.urlopen('http://www.sina.com.cn/') as response:
   data = response.read()
   html = data.decode()
   print(html)