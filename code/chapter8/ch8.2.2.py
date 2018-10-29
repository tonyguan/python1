# coding=utf-8
# 代码文件：chapter8/ch8.2.2.py

print("----范围-------")
for num in range(1, 10):  # 使用范围
    print("{0} x {0} = {1}".format(num, num * num))

print("----字符串-------")
#  for语句
for item in 'Hello':
    print(item)

# 声明整数列表
numbers = [43, 32, 53, 54, 75, 7, 10]

print("----整数列表-------")

#  for语句
for item in numbers:
    print("Count is : {0}".format(item))
