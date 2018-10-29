# coding=utf-8
# 代码文件：chapter12/ch12.5.py

import datetime as dt
import traceback as tb

def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except (ValueError, OSError) as e:
        print('调用方法method1处理...')
        tb.print_exc()


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
