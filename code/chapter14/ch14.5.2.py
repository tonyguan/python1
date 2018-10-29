# coding=utf-8
# 代码文件：chapter14/ch14.5.2.py


import re

p = r'[Jj]ava'
text = 'I like Java and java.'

match_list = re.findall(p, text)
print(match_list)  # 匹配

match_iter = re.finditer(p, text)
for m in match_iter:
    print(m.group())
