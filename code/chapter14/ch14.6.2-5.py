# coding=utf-8
# 代码文件：chapter14/ch14.6.2-5.py

import re

p = """(java)     #匹配java字符串
        .*        #匹配任意字符零或多个
        (python)  #匹配python字符串
    """

regex = re.compile(p, re.I | re.VERBOSE)

m = regex.search('I like Java and Python.')
print(m)  # 匹配

m = regex.search('I like JAVA and Python.')
print(m)  # 匹配

m = regex.search('I like java and Python.')
print(m)  # 匹配
