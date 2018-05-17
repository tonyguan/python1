# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.8.2.py

import enum


@enum.unique
class WeekDays(enum.IntEnum):
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3  # 'Wed.'
    THURSDAY = 4
    FRIDAY = 5  # 1


day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)
