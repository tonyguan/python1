# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

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
