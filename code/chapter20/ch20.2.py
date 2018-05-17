# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter20/ch20.2.py

import threading

# 当前线程对象
t = threading.current_thread()
# 当前线程名
print(t.name)

# 返回当前处于活动状态的线程个数
print(threading.active_count())

# 当主线程对象
t = threading.main_thread()
# 主线程名
print(t.name)
