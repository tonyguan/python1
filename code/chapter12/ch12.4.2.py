# coding=utf-8
# 代码文件：chapter12/ch12.4.2.py

import datetime as dt


def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
        print(e)
    except FileNotFoundError as e:
        print('处理FileNotFoundError异常')
        print(e)
    except OSError as e:
        print('处理OSError异常')
        print(e)


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
