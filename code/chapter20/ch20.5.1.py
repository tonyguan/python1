# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter20/ch20.5.1.py

import threading
import time


class TicketDB:
    def __init__(self):
        # 机票的数量
        self.ticket_count = 5

    # 获得当前机票数量
    def get_ticket_count(self):
        return self.ticket_count

    # 销售机票
    def sell_ticket(self):
        # TODO 等于用户付款
        # 线程休眠，阻塞当前线程，模拟等待用户付款
        time.sleep(1)
        print("第{0}号票,已经售出".format(self.ticket_count))
        self.ticket_count -= 1


# 创建TicketDB对象
db = TicketDB()


# 线程体1函数
def thread1_body():
    global db  # 声明为全局变量
    while True:
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            # 无票退出
            break


# 线程体2函数
def thread2_body():
    global db  # 声明为全局变量
    while True:
        curr_ticket_count = db.get_ticket_count()
        # 查询是否有票
        if curr_ticket_count > 0:
            db.sell_ticket()
        else:
            # 无票退出
            break


# 主函数
def main():
    # 创建线程对象t1
    t1 = threading.Thread(target=thread1_body)
    # 启动线程t1
    t1.start()
    # 创建线程对象t2
    t2 = threading.Thread(target=thread2_body)
    # 启动线程t2
    t2.start()


if __name__ == '__main__':
    main()
