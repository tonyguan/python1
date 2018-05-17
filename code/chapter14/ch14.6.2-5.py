# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

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
