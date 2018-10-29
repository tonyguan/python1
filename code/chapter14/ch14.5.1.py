# coding=utf-8
# 代码文件：chapter14/ch14.5.1.py


import re

p = r'\w+@zhijieketang\.com'

text = "Tony's email is tony_guan588@zhijieketang.com."
m = re.search(p, text)
print(m)  # 匹配

m = re.match(p, text)
print(m)  # 不匹配

email = 'tony_guan588@zhijieketang.com'
m = re.search(p, email)
print(m)  # 匹配

m = re.match(p, email)
print(m)  # 匹配

# match对象几个方法
print('match对象几个方法:')
print(m.group())
print(m.start())
print(m.end())
print(m.span())
