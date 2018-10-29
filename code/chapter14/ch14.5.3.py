# coding=utf-8
# 代码文件：chapter14/ch14.5.3.py


import re

p = r'\d+'
text = 'AB12CD34EF'

clist = re.split(p, text)
print(clist)

clist = re.split(p, text, maxsplit=1)
print(clist)

clist = re.split(p, text, maxsplit=2)
print(clist)
