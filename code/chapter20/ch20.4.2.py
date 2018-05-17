# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter20/ch20.4.2.py

import threading
import time

# 线程停止变量
isrunning = True


# 线程体函数
def thread_body():
    while isrunning:
        # 线程开始工作
        # TODO
        print('下载中...')
        # 线程休眠
        time.sleep(5)
    print('执行完成!')


# 主函数
def main():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread_body)
    # 启动线程t1
    t1.start()
    # 从键盘输入停止指令 exit
    command = input('请输入停止指令：')
    if command == 'exit':
        global isrunning
        isrunning = False


if __name__ == '__main__':
    main()
