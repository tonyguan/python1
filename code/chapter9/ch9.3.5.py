# coding=utf-8
# 代码文件：chapter9/ch9.3.5.py

n_set = {x for x in range(100) if x % 2 == 0 if x % 5 == 0}
print(n_set)

input_list = [2, 3, 2, 4, 5, 6, 6, 6]

n_list = [x ** 2 for x in input_list]
print(n_list)

n_set = {x ** 2 for x in input_list}
print(n_set)
