# coding=utf-8
# 代码文件：chapter11/ch11.7.1.py


class Person:
    def __init__(self, name, age):
        self.name = name  # 名字
        self.age = age  # 年龄

    def __str__(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s


person = Person('Tony', 18)
print(person)
