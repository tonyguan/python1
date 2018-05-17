# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter8/ch8.1.1.py

import sys

# print(sys.argv[:])

score = int(sys.argv[1])  # 获得命令行传入的参数

if score >= 85:
    print("您真优秀！")

if score < 60:
    print("您需要加倍努力！")

if (score >= 60) and (score < 85):
    print("您的成绩还可以，仍需继续努力！")
