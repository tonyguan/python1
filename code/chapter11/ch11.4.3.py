# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.4.3.py

# class Animal(object):
#     """定义动物类"""
#
#     def __init__(self, age, sex=1, weight=0.0):
#         self.age = age  # 定义年龄实例成员变量
#         self.sex = sex  # 定义性别实例成员变量
#         self.__weight = weight  # 定义体重实例成员变量
#
#     def set_weight(self, weight):
#         self.__weight = weight
#
#     def get_weight(self):
#         return self.__weight
#
#
# a1 = Animal(2, 0, 10.0)
# print('a1体重：{0:0.2f}'.format(a1.get_weight()))
# a1.set_weight(123.45)
# print('a1体重：{0:0.2f}'.format(a1.get_weight()))

class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例成员变量
        self.sex = sex  # 定义性别实例成员变量
        self.__weight = weight  # 定义体重实例成员变量

    @property
    def weight(self):  # 替代get_weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):  # 替代set_weight(self, weight):
        self.__weight = weight


a1 = Animal(2, 0, 10.0)
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.weight = 123.45  # a1.set_weight(123.45)
print('a1体重：{0:0.2f}'.format(a1.weight))
