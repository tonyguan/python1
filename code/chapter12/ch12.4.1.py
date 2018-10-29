# coding=utf-8
# 代码文件：chapter12/ch12.4.1.py
import datetime as dt

str_date = '2011-13-18'
in_date = dt.datetime.strptime(str_date, '%Y-%m-%d')
print(in_date)
