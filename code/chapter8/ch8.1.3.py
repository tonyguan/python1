# coding=utf-8
# 代码文件：chapter8/ch8.1.3.py

import sys

score = int(sys.argv[1])  # 获得命令行传入的参数

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade = " + grade)
