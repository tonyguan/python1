# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter10/ch10.7.3.py

from functools import reduce

# 1.filter()
users = ['Tony', 'Tom', 'Ben', 'Alex']

users_filter = filter(lambda u: u.startswith('T'), users)
print(list(users_filter))

number_list = range(1, 11)
nmber_filter = filter(lambda it: it % 2 == 0, number_list)
print(list(nmber_filter))

# 2.map()
users_map = map(lambda u: u.lower(), users)
print(list(users_map))

# users_map = map(lambda u: u.lower(), users_filter)
users_map = map(lambda u: u.lower(), filter(lambda u: u.startswith('T'), users))

print(list(users_map))


# 3.reduce()
a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)  # 10
# a_reduce = reduce(lambda acc, i: acc + i, a, 2)  # 12
print(a_reduce)
