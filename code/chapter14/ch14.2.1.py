# coding=utf-8
# 代码文件：chapter14/ch14.2.1.py


import re

p = r'[Jj]ava'
# p = r'Java|java|JAVA'

m = re.search(p, 'I like Java and Python.')
print(m)  # 匹配

m = re.search(p, 'I like JAVA and Python.')
print(m)  # 不匹配

m = re.search(p, 'I like java and Python.')
print(m)  # 匹配
