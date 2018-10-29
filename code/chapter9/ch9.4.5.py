# coding=utf-8
# 代码文件：chapter9/ch9.4.5.py

input_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

output_dict = {k: v for k, v in input_dict.items() if v % 2 == 0}
print(output_dict)

keys = [k for k, v in input_dict.items() if v % 2 == 0]
print(keys)
