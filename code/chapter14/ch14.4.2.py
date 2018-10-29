# coding=utf-8
# 代码文件：chapter14/ch14.4.2.py


import re

p = r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'
m = re.search(p, '010-87654321')
print(m)  # 匹配
print(m.group())  # 返回匹配字符串
print(m.groups())  # 获得所有组内容

# 通过组编号返回组内容
print(m.group(1))
print(m.group(2))

# 通过组名返回组内容
print(m.group('area_code'))
print(m.group('phone_code'))
