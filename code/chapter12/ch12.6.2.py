# coding=utf-8
# 代码文件：chapter12/ch12.6.2.py

import datetime as dt


def read_date_from_file(filename):
    try:
        file = open(filename)
    except OSError as e:
        print('打开文件失败')
    else:
        print('打开文件成功')
        try:
            in_date = file.read()
            in_date = in_date.strip()
            date = dt.datetime.strptime(in_date, '%Y-%m-%d')
            return date
        except ValueError as e:
            print('处理ValueError异常')
        except OSError as e:
            print('处理OSError异常')
        finally:
            file.close()


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
