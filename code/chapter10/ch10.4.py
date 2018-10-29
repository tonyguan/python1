# coding=utf-8
# 代码文件：chapter9/ch10.4.py

# 创建全局变量x
x = 20


def print_value():
    global x
    x = 10
    print("函数中x = {0}".format(x))


print_value()
print("全局变量x = {0}".format(x))
