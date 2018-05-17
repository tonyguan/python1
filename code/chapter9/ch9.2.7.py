# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter9/ch9.2.7.py

n_list = []
for x in range(10):
    if x % 2 == 0:
        n_list.append(x ** 2)
print(n_list)

n_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(n_list)

n_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(n_list)
