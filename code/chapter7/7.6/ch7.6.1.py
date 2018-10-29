# coding=utf-8
# 代码文件：chapter7/7.6/ch7.6.1.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


p1 = Person('Tony', 18)
p2 = Person('Tony', 18)

print(p1 == p2)  # True
print(p1 is p2)  # False

print(p1 != p2)  # False
print(p1 is not p2)  # True
