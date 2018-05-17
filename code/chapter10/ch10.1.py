# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter10/ch10.1.py


def rectangle_area(width, height):
    area = width * height
    return area


r_area = rectangle_area(320.0, 480.0)

print("320x480的长方形的面积:{0:.2f}".format(r_area))
