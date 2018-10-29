# coding=utf-8
# 代码文件：chapter22/ch22.2.4.py

import csv

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import mpl_finance
import pandas

from db.db_access import findall_hisq_data

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def pot_candlestick_ohlc(datafile):
    """绘制K线图"""

    # 从CSV文件中读入数据DataFrame数据结构中
    quotes = pandas.read_csv(datafile,
                             index_col=0,
                             parse_dates=True,
                             infer_datetime_format=True)

    # 绘制一个子图，并设置子图大小
    fig, ax = plt.subplots(figsize=(10, 5))
    # 调整子图参数SubplotParams
    fig.subplots_adjust(bottom=0.2)

    mpl_finance.candlestick_ohlc(ax, zip(mdates.date2num(quotes.index.to_pydatetime()),
                                         quotes['Open'], quotes['High'],
                                         quotes['Low'], quotes['Close']),
                                 width=1, colorup='r', colordown='g')

    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()


def main():
    """主函数"""

    data = findall_hisq_data('AAPL')

    # 列名
    colsname = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # 临时数据文件名
    datafile = 'temp.csv'
    # 写如数据到临时数据文件
    with open(datafile, 'w', newline='', encoding='utf-8') as wf:
        writer = csv.writer(wf)
        writer.writerow(colsname)
        for quotes in data:
            row = [quotes['Date'], quotes['Open'], quotes['High'],
                   quotes['Low'], quotes['Close'], quotes['Volume']]
            writer.writerow(row)

    # 调用绘图函数
    pot_candlestick_ohlc(datafile)


if __name__ == '__main__':
    main()
