# coding=utf-8
# 代码文件：chapter10/ch10.7.2.py


def calculate_fun(opr):
    if opr == '+':
        return lambda a, b: (a + b)
    else:
        return lambda a, b: (a - b)


f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f1))

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
