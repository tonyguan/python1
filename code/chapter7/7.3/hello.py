# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter7/7.3/hello.py

i = 0
a = 10
b = 9

if a > b or i == 1:
    print("或运算为 真")
else:
    print("或运算为 假")

if a < b and i == 1:
    print("与运算为 真")
else:
    print("与运算为 假")


def f1():
    return a > b


def f2():
    print('--f2--')
    return a == b


print(f1() or f2())
