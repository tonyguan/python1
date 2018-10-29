# coding=utf-8
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
