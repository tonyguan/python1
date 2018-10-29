# coding=utf-8
# 代码文件：chapter11/ch11.8.1.py

import enum


class WeekDays(enum.Enum):
    # 枚举常量列表
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 10


day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)