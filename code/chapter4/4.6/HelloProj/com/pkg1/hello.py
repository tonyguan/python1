# coding=utf-8
# 代码文件：chapter4/4.5/com/pkg1/hello.py

import com.pkg2.hello as module1
from com.pkg2.hello import z

y = 20

print(y)  # 访问当前模块变量y
print(module1.y)  # 访问com.pkg2.hello模块变量y
print(z)  # 访问com.pkg2.hello模块变量z
