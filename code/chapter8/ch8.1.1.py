# coding=utf-8
# 代码文件：chapter8/ch8.1.1.py

import sys

# print(sys.argv[:])

score = int(sys.argv[1])  # 获得命令行传入的参数

if score >= 85:
    print("您真优秀！")

if score < 60:
    print("您需要加倍努力！")

if (score >= 60) and (score < 85):
    print("您的成绩还可以，仍需继续努力！")
