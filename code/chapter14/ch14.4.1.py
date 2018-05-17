# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.4.1.py


import re

p = r'(121){2}'
m = re.search(p, '121121abcabc')
print(m)  # 匹配
print(m.group())  # 返回匹配字符串
print(m.group(1))  # 获得第一组内容

p = r'(\d{3,4})-(\d{7,8})'
m = re.search(p, '010-87654321')
print(m)  # 匹配
print(m.group())  # 返回匹配字符串
print(m.groups())  # 获得所有组内容
