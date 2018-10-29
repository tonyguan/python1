# coding=utf-8
# 代码文件：chapter14/ch14.1.3.py


import re

p1 = r'\w+@zhijieketang\.com'
p2 = r'^\w+@zhijieketang\.com$'

text = "Tony's email is tony_guan588@zhijieketang.com."
m = re.search(p1, text)
print(m)  # 匹配
m = re.search(p2, text)
print(m)  # 不匹配

email = 'tony_guan588@zhijieketang.com'
m = re.search(p2, email)
print(m)  # 匹配
