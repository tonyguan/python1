# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter8/ch8.1.2.py

import sys

score = int(sys.argv[1])  # 获得命令行传入的参数

if score >= 60:
    print("及格")
    if score >= 90:
        print("优秀")
else:
    print("不及格")