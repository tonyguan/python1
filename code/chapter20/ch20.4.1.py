# coding=utf-8
# 代码文件：chapter20/ch20.4.1.py

import threading
import time

# 共享变量
value = 0


# 线程体函数
def thread_body():
    global value
    # 当前线程对象
    print('ThreadA 开始...')
    for n in range(2):
        print('ThreadA 执行...')
        value += 1
        # 线程休眠
        time.sleep(1)
    print('ThreadA 结束...')


# 主函数
def main():
    print('主线程 开始...')
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_body, name='ThreadA')
    # 启动线程t1
    t1.start()
    # 主线程被阻塞，等待t1线程结束
    t1.join()
    print('value = {0}'.format(value))
    print('主线程 结束...')


if __name__ == '__main__':
    main()
