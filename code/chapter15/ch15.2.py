# coding=utf-8
# 代码文件：chapter15/ch15.2.py

import os

f_name = 'test.txt'
copy_f_name = 'copy.txt'

with open(f_name, 'r') as f:
    b = f.read()
    with open(copy_f_name, 'w') as copy_f:
        copy_f.write(b)

try:
    os.rename(copy_f_name, 'copy2.txt')
except OSError:
    os.remove('copy2.txt')

print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

try:
    os.mkdir('subdir')
except OSError:
    os.rmdir('subdir')

for item in os.walk('.'):
    print(item)
