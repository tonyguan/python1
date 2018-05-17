# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter10/ch10.2.1.py


def print_area(width, height):
    area = width * height
    print("{0} x {1} 长方形的面积:{2}".format(width, height, area))


print_area(320.0, 480.0)  # 没有采用关键字参数函数调用
print_area(width=320.0, height=480.0)  # 采用关键字参数函数调用
print_area(320.0, height=480.0)  # 采用关键字参数函数调用
# print_area(width=320.0, height)  # 发生错误
print_area(height=480.0, width=320.0)  # 采用关键字参数函数调用
