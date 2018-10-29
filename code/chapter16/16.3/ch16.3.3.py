# coding=utf-8
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