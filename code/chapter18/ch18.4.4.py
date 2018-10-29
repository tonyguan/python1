# coding=utf-8
# 代码文件：chapter18/ch18.4.4.py

import urllib.request
import urllib.parse

url = 'http://www.51work6.com/service/mynotes/WebService.php'
params_dict = {'email': <换成自己的注册邮箱>, 'type': 'JSON', 'action': 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)

url = url + '?' + params_str  # HTTP参数放到URL之后
print(url)

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
