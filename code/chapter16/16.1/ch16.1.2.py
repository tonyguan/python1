# coding=utf-8
# 代码文件：chapter16/16.1/ch16.1.2.py

import csv

with open('data/books.csv', 'r', encoding='gbk') as rf:
    reader = csv.reader(rf)
    with open('data/books2.csv', 'w', newline='', encoding='gbk') as wf:
        writer = csv.writer(wf, delimiter='\t')
        for row in reader:
            print('|'.join(row))
            writer.writerow(row)
