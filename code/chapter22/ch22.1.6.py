# coding=utf-8
# 代码文件：chapter22/ch22.1.6.py

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)

plt.scatter(x, y)

plt.title('绘制散点图')

plt.show()  # 显示图形
