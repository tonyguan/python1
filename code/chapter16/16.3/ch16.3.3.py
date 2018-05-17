# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/ch16.3.3.py

import json

# 准备数据
json_obj = r'{"name": "tony", "age": 30, "sex": true, "a": [1, 3], "b": ["A", "B", "C"]}'
#json_obj = "{'name': 'tony', 'age': 30, 'sex': true, 'a': [1, 3], 'b': ['A', 'B', 'C']}"

py_dict = json.loads(json_obj)
print(type(py_dict))  # <class 'dict'>
print(py_dict['name'])
print(py_dict['age'])
print(py_dict['sex'])

py_lista = py_dict['a']  # 取出列表对象
print(py_lista)
py_listb = py_dict['b']  # 取出列表对象
print(py_listb)

# 读取JSON数据到data2.json文件
with open('data/data2.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))  # <class 'dict'>