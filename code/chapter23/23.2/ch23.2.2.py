# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter23/23.2/ch23.2.2.py

import matplotlib.pyplot as plt

from db.db_access import findall_hisq_data


def pot_hisvolume(dates, volumes):
    """苹果股票历史成交量折线图"""

    # 设置中文字体
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置图表大小
    plt.figure(figsize=(10, 5))

    # 绘制线段
    plt.plot(dates, volumes)

    plt.title('苹果股票历史成交量')  # 添加图表标题
    plt.ylabel('成交量')  # 添加y轴标题
    plt.xlabel('交易日期')  # 添加x轴标题

    plt.show()  # 显示图形


def main():
    """主函数"""

    data = findall_hisq_data('AAPL')

    # 从data中提取成交量数据
    volume_map = map(lambda it: it['Volume'], data)
    # 将volume_map转换为交量列表
    volume_list = list(volume_map)

    # 从data中提取日期数据
    date_map = map(lambda it: it['Date'], data)
    # 将date_map转换为日期列表
    date_list = list(date_map)

    pot_hisvolume(date_list, volume_list)


if __name__ == '__main__':
    main()
