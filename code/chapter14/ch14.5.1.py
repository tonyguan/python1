# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

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
