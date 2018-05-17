# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter13/ch13.2.py


import random

# 0.0 <= x < 1.0随机数
print('0.0 <= x < 1.0随机数')
for i in range(0, 10):
    x = random.random()
    print(x)

# 0 <= x < 5随机数
print('0 <= x < 5随机数')
for i in range(0, 10):
    x = random.randrange(5)
    print(x, end=' ')

# 5 <= x < 10随机数
print()
print('5 <= x < 10随机数')
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x, end=' ')

# 5 <= x <= 10随机数
print()
print('5 <= x <= 10随机数')
for i in range(0, 10):
    x = random.randint(5, 10)
    print(x, end=' ')
