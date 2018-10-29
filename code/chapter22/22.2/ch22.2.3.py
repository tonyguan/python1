# coding=utf-8
# 代码文件：chapter22/23.2/ch22.2.3.py

import matplotlib.pyplot as plt

from db.db_access import findall_hisq_data

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def pot_his_bar(date_list, p_list, ylabel):
    """绘制OHLC柱状图"""

    # 绘制柱状图
    plt.bar(date_list, p_list)

    plt.title('苹果股票历史成交量')  # 添加图表标题
    plt.ylabel(ylabel)  # 添加y轴标题
    plt.xlabel('交易日期')  # 添加x轴标题


def main():
    """主函数"""

    data = findall_hisq_data('AAPL')

    # 从data中提取日期数据
    date_map = map(lambda it: it['Date'], data)
    # 将date_map转换为日期列表
    date_list = list(date_map)

    # 从data中提取开盘价数据
    open_map = map(lambda it: it['Open'], data)
    # 将open_map转换为开盘价列表
    open_list = list(open_map)

    # 从data中提取成最高价数据
    high_map = map(lambda it: it['High'], data)
    # 将high_map转换为最高价列表
    high_list = list(high_map)

    # 从data中提取最低价数据
    low_map = map(lambda it: it['Low'], data)
    # 将open_map转换为最低价列表
    low_list = list(low_map)

    # 从data中提取收盘价数据
    close_map = map(lambda it: it['Close'], data)
    # 将open_map转换为收盘价列表
    close_list = list(close_map)

    # 设置图表大小
    plt.figure(figsize=(10, 6))

    plt.subplot(411)
    pot_his_bar(date_list, open_list, '开盘价')

    plt.subplot(412)
    pot_his_bar(date_list, close_list, '收盘价')

    plt.subplot(413)
    pot_his_bar(date_list, high_list, '最高价')

    plt.subplot(414)
    pot_his_bar(date_list, low_list, '最低价')

    plt.tight_layout()  # 调整布局
    plt.show()  # 显示图形


if __name__ == '__main__':
    main()
