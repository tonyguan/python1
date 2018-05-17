# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/16.1/ch16.1.1.py

import csv

with open('data/books.csv', 'r',  encoding='gbk') as rf:
    reader = csv.reader(rf, dialect=csv.excel)
    for row in reader:
        print('|'.join(row))
