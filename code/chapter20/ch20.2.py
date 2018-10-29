# coding=utf-8
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
