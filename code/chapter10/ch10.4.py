# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter9/ch10.4.py

# 创建全局变量x
x = 20


def print_value():
    global x
    x = 10
    print("函数中x = {0}".format(x))


print_value()
print("全局变量x = {0}".format(x))
