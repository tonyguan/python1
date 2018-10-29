# coding=utf-8
# 代码文件：chapter22/ch22.1.5.py

import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']

# 各种活动标题列表
activies = ['工作', '睡', '吃', '玩']
# 各种活动所占时间列表
slices = [8, 7, 3, 6]
# 各种活动在饼状图中的颜色列表
cols = ['c', 'm', 'r', 'b']

plt.pie(slices, labels=activies, colors=cols,
        shadow=True, explode=(0, 0.1, 0, 0), autopct='%.1f%%')

plt.title('绘制饼状图')

plt.show()  # 显示图形
