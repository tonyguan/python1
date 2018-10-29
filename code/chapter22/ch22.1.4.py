# coding=utf-8
# 代码文件：chapter22/ch22.1.4.py

import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']

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

plt.legend()  # 设置图例

plt.show()  # 显示图形
