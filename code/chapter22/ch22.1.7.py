# coding=utf-8
# 代码文件：chapter22/ch22.1.7.py

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def drowsubbar():
    """绘制饼状图"""

    x1 = [1, 3, 5, 7, 9]  # x1轴坐标数据
    y1 = [5, 2, 7, 8, 2]  # y1轴坐标数据

    x2 = [2, 4, 6, 8, 10]  # x2轴坐标数据
    y2 = [8, 6, 2, 5, 6]  # y2轴坐标数据

    # 绘制柱状图
    plt.bar(x1, y1, label='柱状图1')
    plt.bar(x2, y2, label='柱状图2')

    plt.title('绘制柱状图')  # 添加图表标题

    plt.ylabel('y轴')  # 添加y轴标题
    plt.xlabel('x轴')  # 添加x轴标题

    plt.title('绘制散点图')


def drowsubpie():
    """绘制饼状图"""

    # 各种活动标题列表
    activies = ['工作', '睡', '吃', '玩']
    # 各种活动所占时间列表
    slices = [8, 7, 3, 6]
    # 各种活动在饼状图中的颜色列表
    cols = ['c', 'm', 'r', 'b']

    plt.pie(slices, labels=activies, colors=cols,
            shadow=True, explode=(0, 0.1, 0, 0), autopct='%.1f%%')

    plt.title('绘制饼状图')


def drowsubline():
    """绘制折线图"""

    x = [5, 4, 2, 1]  # x轴坐标数据
    y = [7, 8, 9, 10]  # y轴坐标数据

    # 绘制线段
    plt.plot(x, y, 'b', label='线1', linewidth=2)

    plt.title('绘制折线图')  # 添加图表标题

    plt.ylabel('y轴')  # 添加y轴标题
    plt.xlabel('x轴')  # 添加x轴标题

    plt.legend()  # 设置图例


def drowssubscatter():
    """绘制散点图"""

    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)

    plt.scatter(x, y)

    plt.title('绘制散点图')


plt.subplot(2, 2, 1)  # 替换(221)
drowsubbar()

plt.subplot(2, 2, 2)  # 替换(222)
drowsubpie()

plt.subplot(2, 2, 3)  # 替换(223)
drowsubline()

plt.subplot(2, 2, 4)  # 替换(224)
drowssubscatter()

plt.tight_layout()  # 调整布局

plt.show()  # 显示图形
