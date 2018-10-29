# coding=utf-8
# 代码文件：chapter12/ch12.7.py


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
