# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.3.1.py


import re

m = re.search(r'\d?', '87654321')  # 出现数字一次
print(m)  # 匹配字符'8'

m = re.search(r'\d?', 'ABC')  # 出现数字零次
print(m)  # 匹配字符''

m = re.search(r'\d*', '87654321')  # 出现数字多次
print(m)  # 匹配字符'87654321'

m = re.search(r'\d*', 'ABC')  # 出现数字零次
print(m)  # 匹配字符''

m = re.search(r'\d+', '87654321')  # 出现数字多次
print(m)  # 匹配字符'87654321'

m = re.search(r'\d+', 'ABC')
print(m)  # 不匹配

m = re.search(r'\d{8}', '87654321')  # 出现数字8次
print('8765432', m)  # 匹配字符'87654321'

m = re.search(r'\d{8}', 'ABC')
print(m)  # 不匹配

m = re.search(r'\d{7,8}', '87654321')  # 出现数字8次
print(m)  # 匹配字符'87654321'

m = re.search(r'\d{9,}', '87654321')
print(m)  # 不匹配
