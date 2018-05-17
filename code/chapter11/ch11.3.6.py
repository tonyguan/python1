# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.3.6.py


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.weight = weight  # 定义体重实例变量

    def eat(self):
        self.weight += 0.05
        print('eat...')

    def run(self):
        self.weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.eat()
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.run()
print('a1体重：{0:0.2f}'.format(a1.weight))
