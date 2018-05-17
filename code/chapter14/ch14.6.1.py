# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.6.1.py


import re

p = r'\w+@zhijieketang\.com'
regex = re.compile(p)

text = "Tony's email is tony_guan588@zhijieketang.com."
m = regex.search(text)
print(m)  # 匹配

m = regex.match(text)
print(m)  # 不匹配

p = r'[Jj]ava'
regex = re.compile(p)
text = 'I like Java and java.'

match_list = regex.findall(text)
print(match_list)  # 匹配

match_iter = regex.finditer(text)
for m in match_iter:
    print(m.group())

p = r'\d+'
regex = re.compile(p)
text = 'AB12CD34EF'

clist = regex.split(text)
print(clist)

repace_text = regex.sub(' ', text)
print(repace_text)
