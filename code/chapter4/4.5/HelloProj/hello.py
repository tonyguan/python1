# coding=utf-8
# 代码文件：chapter4/4.5/hello.py

import module1
from module1 import z

y = 20

print(y)  # 访问当前模块变量y
print(module1.y)  # 访问module1模块变量y
print(z)  # 访问module1模块变量z
