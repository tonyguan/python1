# coding=utf-8
# 代码文件：chapter14/ch14.6.2-1.py


import re

text = '你们好Hello'

p = r'\w+'
regex = re.compile(p, re.U)

m = regex.search(text)
print(m)  # 匹配

m = regex.match(text)
print(m)  # 匹配

regex = re.compile(p, re.A)

m = regex.search(text)
print(m)  # 匹配

m = regex.match(text)
print(m)  # 不匹配
