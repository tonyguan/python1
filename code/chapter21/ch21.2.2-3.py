# coding=utf-8
# 代码文件：chapter21/ch21.2.2-3.py

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
