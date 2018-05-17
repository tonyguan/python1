# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter22/ch22.2.2-2.py

"""获得动态数据"""
import re
import urllib.request

url = 'http://q.stock.sohu.com/hisHq?code=cn_600519&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.8115656498417958'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode('gbk')
    print(htmlstr)
    htmlstr = htmlstr.replace('historySearchHandler(', '')
    htmlstr = htmlstr.replace(')', '')
    print('替换后的：', htmlstr)
