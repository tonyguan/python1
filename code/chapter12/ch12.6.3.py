# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter12/ch12.6.3.py

import datetime as dt


def read_date_from_file(filename):
    try:
        with open(filename) as file:
            in_date = file.read()

        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理ValueError异常')
    except OSError as e:
        print('处理OSError异常')


date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))
