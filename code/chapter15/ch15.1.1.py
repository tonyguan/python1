# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter15/ch15.1.1.py


f = open('test.txt', 'w+')
f.write('World')

f = open('test.txt', 'r+')
f.write('Hello')

f = open('test.txt', 'a')
f.write(' ')

fname = r'C:\Users\win-mini\PycharmProjects\HelloProj\test.txt'
f = open(fname, 'a+')
f.write('World')
