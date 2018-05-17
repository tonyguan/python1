# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.3.2.py


import re

# 使用贪婪量词
m = re.search(r'\d{5,8}', '87654321')  # 出现数字8次
print(m)  # 匹配字符'87654321'

# 使用惰性量词
m = re.search(r'\d{5,8}?', '87654321')  # 出现数字5次
print(m)  # 匹配字符'87654'
