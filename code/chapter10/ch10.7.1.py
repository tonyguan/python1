# coding=utf-8
# 代码文件：chapter10/ch10.7.1.py


def calculate_fun(opr):
    # 定义相加函数
    def add(a, b):
        return a + b

    # 定义相减函数
    def sub(a, b):
        return a - b

    if opr == '+':
        return add
    else:
        return sub


f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f1))

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
