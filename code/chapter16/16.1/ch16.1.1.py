# coding=utf-8
# 代码文件：chapter16/16.1/ch16.1.1.py

import csv

with open('data/books.csv', 'r',  encoding='gbk') as rf:
    reader = csv.reader(rf, dialect=csv.excel)
    for row in reader:
        print('|'.join(row))
