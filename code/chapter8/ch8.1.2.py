# coding=utf-8
# 代码文件：chapter8/ch8.1.2.py

import sys

score = int(sys.argv[1])  # 获得命令行传入的参数

if score >= 60:
    print("及格")
    if score >= 90:
        print("优秀")
else:
    print("不及格")