# coding=utf-8
# 代码文件：chapter10/ch10.1.py


def rectangle_area(width, height):
    area = width * height
    return area


r_area = rectangle_area(320.0, 480.0)

print("320x480的长方形的面积:{0:.2f}".format(r_area))
