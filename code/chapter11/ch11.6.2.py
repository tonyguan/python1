# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses


# 几何图形
class Figure:
    def draw(self):
        print('绘制Figure...')


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse...')


# 三角形
class Triangle(Figure):
    def draw(self):
        print('绘制Triangle...')


f1 = Figure()  # 没有发生多态
f1.draw()

f2 = Ellipse()  # 发生多态
f2.draw()

f3 = Triangle()  # 发生多态
f3.draw()

print(isinstance(f1, Triangle))  # False
print(isinstance(f2, Triangle))  # False
print(isinstance(f3, Triangle))  # True
print(isinstance(f2, Figure))  # True

print(issubclass(Ellipse, Triangle))  # False
print(issubclass(Ellipse, Figure))  # True
print(issubclass(Triangle, Ellipse))  # False
