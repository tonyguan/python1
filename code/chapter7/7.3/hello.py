# coding=utf-8
# 代码文件：chapter7/7.3/hello.py

i = 0
a = 10
b = 9

if a > b or i == 1:
    print("或运算为 真")
else:
    print("或运算为 假")

if a < b and i == 1:
    print("与运算为 真")
else:
    print("与运算为 假")


def f1():
    return a > b


def f2():
    print('--f2--')
    return a == b


print(f1() or f2())
