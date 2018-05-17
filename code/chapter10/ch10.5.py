# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter23/ch23.2.1.py


# def square(num):
#     n_list = []
#
#     for i in range(1, num + 1):
#         n_list.append(i * i)
#
#     return n_list


def square(num):

    for i in range(1, num + 1):
        yield i * i


for i in square(5):
    print(i, end=' ')
