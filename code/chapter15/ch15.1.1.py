# coding=utf-8
# 代码文件：chapter15/ch15.1.1.py


f = open('test.txt', 'w+')
f.write('World')

f = open('test.txt', 'r+')
f.write('Hello')

f = open('test.txt', 'a')
f.write(' ')

fname = r'C:\Users\win-mini\PycharmProjects\HelloProj\test.txt'
f = open(fname, 'a+')
f.write('World')
