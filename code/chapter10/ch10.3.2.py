# coding=utf-8
# 代码文件：chapter9/ch10.3.2.py


def position(dt, speed):
    posx = speed[0] * dt
    posy = speed[1] * dt
    return (posx, posy)


move = position(60.0, (10, -5))

print("物体位移：({0}, {1})".format(move[0], move[1]))
