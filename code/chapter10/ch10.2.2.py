# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter9/ch10.2.2.py


def make_coffee(name="卡布奇诺"):
    return "制作一杯{0}咖啡。".format(name)


coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()

print(coffee1)  # 制作一杯拿铁咖啡。
print(coffee2)  # 制作一杯卡布奇诺咖啡。
