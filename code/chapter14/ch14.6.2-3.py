# coding=utf-8
# 代码文件：chapter14/ch14.6.2-3.py

import re

p = r'.+'
regex = re.compile(p)

m = regex.search('Hello\nWorld.')
print(m)  # 匹配

regex = re.compile(p, re.DOTALL)

m = regex.search('Hello\nWorld.')
print(m)  # 匹配
