# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/ch16.3.2.py

import json

# 准备数据
py_dict = {'name': 'tony', 'age': 30, 'sex': True}  # 创建字典对象
py_list = [1, 3]  # 创建列表对象
py_tuple = ('A', 'B', 'C')  # 创建元组对象

py_dict['a'] = py_list  # 添加列表到字典中
py_dict['b'] = py_tuple  # 添加元组到字典中

print(py_dict)
print(type(py_dict))  # <class 'dict'>

# 编码过程
json_obj = json.dumps(py_dict)
print(json_obj)
print(type(json_obj))  # <class 'str'>

# 编码过程
json_obj = json.dumps(py_dict, indent=4)
# 漂亮的格式化字符串后输出
print(json_obj)

# 写入JSON数据到data1.json文件
with open('data/data1.json', 'w') as f:
    json.dump(py_dict, f)

# 写入JSON数据到data2.json文件
with open('data/data2.json', 'w') as f:
    json.dump(py_dict, f, indent=4)
