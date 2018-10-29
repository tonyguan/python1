# coding=utf-8
# 代码文件：chapter9/ch9.2.7.py

n_list = []
for x in range(10):
    if x % 2 == 0:
        n_list.append(x ** 2)
print(n_list)

n_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(n_list)

n_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(n_list)
