# coding=utf-8
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
