# coding=utf-8
# 代码文件：chapter8/ch8.1.4.py

import sys

score = int(sys.argv[1]) # 获得命令行传入的参数

result = '及格' if score >= 60 else '不及格'
print(result)
