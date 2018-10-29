# coding=utf-8
# 代码文件：chapter11/ch11.8.3.py

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

if day == WeekDays.MONDAY:
    print('工作')
elif day == WeekDays.FRIDAY:
    print('学习')
