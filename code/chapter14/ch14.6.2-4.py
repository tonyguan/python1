# coding=utf-8
# 代码文件：chapter14/ch14.6.2-4.py

import re

p = r'^World'
regex = re.compile(p)

m = regex.search('Hello\nWorld.')
print(m)  # 不匹配

regex = re.compile(p, re.M)

m = regex.search('Hello\nWorld.')
print(m)  # 匹配
