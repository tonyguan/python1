# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter14/ch14.5.2.py


import re

p = r'[Jj]ava'
text = 'I like Java and java.'

match_list = re.findall(p, text)
print(match_list)  # 匹配

match_iter = re.finditer(p, text)
for m in match_iter:
    print(m.group())
