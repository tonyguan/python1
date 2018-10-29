# coding=utf-8
# 代码文件：chapter14/ch14.4.3.py


import re

# p = r'<([\w]+)>.*</([\w]+)>'
p = r'<([\w]+)>.*</\1>'  # 使用反向引用

m = re.search(p, '<a>abc</a>')
print(m)  # 匹配

m = re.search(p, '<a>abc</b>')
print(m)  # 不匹配
