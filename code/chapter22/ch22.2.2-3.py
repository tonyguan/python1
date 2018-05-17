# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter22/ch22.2.2-3.py

import urllib.request


url = 'http://www.ctrip.com/'

req = urllib.request.Request(url)
req.add_header('User-Agent',
               'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1')

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    if htmlstr.find('mobile') != -1:
        print('移动版')
