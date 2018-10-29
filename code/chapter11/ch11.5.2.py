# coding=utf-8
# 代码文件：chapter11/ch11.5.2.py


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print('动物吃...')


class Dog(Animal):
    def eat(self):
        self.weight += 0.1
        print('狗狗吃...')


a1 = Dog(2, 0, 10.0)
a1.eat()
