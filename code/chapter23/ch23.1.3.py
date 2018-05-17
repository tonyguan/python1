# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter23/ch23.1.3.py

import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']

x = [5, 4, 2, 1]  # x轴坐标数据
y = [7, 8, 9, 10]  # y轴坐标数据

# 绘制线段
plt.plot(x, y, 'b', label='线1', linewidth=2)

plt.title('绘制折线图')  # 添加图表标题

plt.ylabel('y轴')  # 添加y轴标题
plt.xlabel('x轴')  # 添加x轴标题

plt.legend()  # 设置图例

# 以分辨率 72 来保存图片
plt.savefig('折线图', dpi=72)

plt.show()  # 显示图形
