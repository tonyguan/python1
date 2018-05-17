# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/ch18.4.5.py

import urllib.request
import urllib.parse

url = 'http://www.51work6.com/service/mynotes/WebService.php'
# 准备HTTP参数
params_dict = {'email': <换成自己的注册邮箱>, 'type': 'JSON', 'action': 'query'}
params_str = urllib.parse.urlencode(params_dict)
print(params_str)
params_bytes = params_str.encode()  # 字符串转换为字节序列对象

req = urllib.request.Request(url, data=params_bytes)  # 发送POST请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode()
    print(json_data)
