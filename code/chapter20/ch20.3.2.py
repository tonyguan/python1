# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter20/ch20.3.2.py

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    # 线程体函数
    def run(self):
        # 当前线程对象
        t = threading.current_thread()
        for n in range(5):
            # 当前线程名
            print('第{0}次执行线程{1}'.format(n, t.name))
            # 线程休眠
            time.sleep(1)
        print('线程{0}执行完成！'.format(t.name))


# 主函数
def main():
    # 创建线程对象t1
    t1 = MyThread()
    # 启动线程t1
    t1.start()

    # 创建线程对象t2
    t2 = MyThread(name='MyThread')
    # 启动线程t2
    t2.start()


if __name__ == '__main__':
    main()
