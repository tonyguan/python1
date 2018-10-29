# coding=utf-8
# 代码文件：chapter14/ch14.2.2.py


import re

p = r'[^0123456789]'

m = re.search(p, '1000')
print(m)  # 不匹配

m = re.search(p, 'Python 3')
print(m)  # 匹配
