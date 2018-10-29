# coding=utf-8
# 代码文件：chapter20/ch20.6.2.py

import threading
import time

event = threading.Event()


class Stack:
    def __init__(self):
        # 堆栈指针初始值为0
        self.pointer = 0
        # 堆栈有5个数字的空间
        self.data = [-1, -1, -1, -1, -1]

    # 压栈方法
    def push(self, c):
        global event
        # 堆栈已满，不能压栈
        while self.pointer == len(self.data):
            # 等待其它线程把数据出栈
            event.wait()
        # 通知其他线程把数据出栈
        event.set()
        # 数据压栈
        self.data[self.pointer] = c
        # 指针向上移动
        self.pointer += 1

    # 出栈方法
    def pop(self):
        global event
        # 堆栈无数据，不能出栈
        while self.pointer == 0:
            # 等待其他线程把数据压栈
            event.wait()
        # 通知其他线程压栈
        event.set()
        # 指针向下移动
        self.pointer -= 1
        # 数据出栈
        data = self.data[self.pointer]
        return data


# 创建堆栈Stack对象
stack = Stack()


# 生产者线程体函数
def producer_thread_body():
    global stack  # 声明为全局变量
    # 产生10个数字
    for i in range(0, 10):
        # 把数字压栈
        stack.push(i)
        # 打印数字
        print('生产：{0}'.format(i))
        # 每产生一个数字线程就睡眠
        time.sleep(1)


# 消费者线程体函数
def consumer_thread_body():
    global stack  # 声明为全局变量
    # 从堆栈中读取数字
    for i in range(0, 10):
        # 从堆栈中读取数字
        x = stack.pop()
        # 打印数字
        print('消费：{0}'.format(x))
        # 每消费一个数字线程就睡眠
        time.sleep(1)


# 主函数
def main():
    # 创建生产者线程对象producer
    producer = threading.Thread(target=producer_thread_body)
    # 启动生产者线程
    producer.start()
    # 创建消费者线程对象consumer
    consumer = threading.Thread(target=consumer_thread_body)
    # 启动消费者线程
    consumer.start()


if __name__ == '__main__':
    main()
