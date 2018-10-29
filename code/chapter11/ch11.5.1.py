# coding=utf-8
# 代码文件：chapter11/ch11.5.1.py


class Person:

    def __init__(self, name, age):
        self.name = name  # 名字
        self.age = age  # 年龄

    def info(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s


p = Person('小赵', 18)
print(p.info())


# class Student:
#
#     def __init__(self, name, age, school):
#         self.name = name  # 名字
#         self.age = age  # 年龄
#         self.school = school  # 所在学校
#
#     def info(self):
#         template = 'Student [name={0}, age={1}, school={2}]'
#         s = template.format(self.name, self.age, self.school)
#         return s

class Student(Person):

    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school  # 所在学校

    # def info(self):
    #     template = 'Student [name={0}, age={1}, school={2}]'
    #     s = template.format(self.name, self.age, self.school)
    #     return s


s = Student('Tom', 28, '清华大学')
print(s.info())
