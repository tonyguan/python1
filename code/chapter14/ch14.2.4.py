# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.2.4.py


import re

# p = r'[^0123456789]'
p = r'\D'

m = re.search(p, '1000')
print(m)  # 不匹配

m = re.search(p, 'Python 3')
print(m)  # 匹配

text = '你们好Hello'
m = re.search(r'\w', text)
print(m)  # 匹配
