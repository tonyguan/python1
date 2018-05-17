# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.6.3.py

class Animal(object):
    def run(self):
        print('动物跑...')


class Dog(Animal):
    def run(self):
        print('狗狗跑...')


class Car:
    def run(self):
        print('汽车跑...')


def go(animal):  # 接收参数是Animal
    animal.run()


go(Animal())
go(Dog())
go(Car())