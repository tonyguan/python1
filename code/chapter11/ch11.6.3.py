# coding=utf-8
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
