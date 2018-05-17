# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter15/ch15.2.py

import os

f_name = 'test.txt'
copy_f_name = 'copy.txt'

with open(f_name, 'r') as f:
    b = f.read()
    with open(copy_f_name, 'w') as copy_f:
        copy_f.write(b)

try:
    os.rename(copy_f_name, 'copy2.txt')
except OSError:
    os.remove('copy2.txt')

print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

try:
    os.mkdir('subdir')
except OSError:
    os.rmdir('subdir')

for item in os.walk('.'):
    print(item)
