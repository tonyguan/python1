# coding=utf-8
# 代码文件：chapter13/ch13.2.py


import random

# 0.0 <= x < 1.0随机数
print('0.0 <= x < 1.0随机数')
for i in range(0, 10):
    x = random.random()
    print(x)

# 0 <= x < 5随机数
print('0 <= x < 5随机数')
for i in range(0, 10):
    x = random.randrange(5)
    print(x, end=' ')

# 5 <= x < 10随机数
print()
print('5 <= x < 10随机数')
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x, end=' ')

# 5 <= x <= 10随机数
print()
print('5 <= x <= 10随机数')
for i in range(0, 10):
    x = random.randint(5, 10)
    print(x, end=' ')
