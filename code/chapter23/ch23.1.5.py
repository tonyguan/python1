# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter23/ch23.1.5.py

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
