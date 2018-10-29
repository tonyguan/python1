# coding=utf-8
# 代码文件：chapter21/21.4/ch21.4.4.py

"""项目实战：抓取纳斯达克股票数据"""

import datetime
import hashlib
import os
import re
import urllib.request

from bs4 import BeautifulSoup

from db.db_access import insert_hisq_data


url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'


def validateUpdate(html):
    """验证数据是否更新，更新返回True，未更新返回False"""
    print(html)
    # 创建md5对象
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code = md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):  # 如果文件存在读取文件内容
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()

    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        # 把新的md5码写入到文件中
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新')
        return True


req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    html = data.decode()

    sp = BeautifulSoup(html, 'html.parser')  
    # 返回指定CSS选择器的div标签列表
    div = sp.select('div#quotes_content_left_pnlAJAX')
    # 从列表中返回第一个元素
    divstring = div[0]

    if validateUpdate(divstring):  # 数据更新
        # 分析数据
        trlist = sp.select('div#quotes_content_left_pnlAJAX table tbody tr')

        data = []

        for tr in trlist:
            trtext = tr.text.strip('\n\r ')
            if trtext == '':
                continue

            rows = re.split(r'\s+', trtext)
            fields = {}
            try:
                df = '%m/%d/%Y'
                fields['Date'] = datetime.datetime.strptime(rows[0], df)
            except ValueError:
                # 实时数据不分析（只有时间，如10:12）
                continue
            fields['Open'] = float(rows[1])
            fields['High'] = float(rows[2])
            fields['Low'] = float(rows[3])
            fields['Close'] = float(rows[4])
            fields['Volume'] = int(rows[5].replace(',', ''))
            data.append(fields)

        print(data)

        # 保存数据到数据库
        for row in data:
            row['Symbol'] = 'AAPL'
            insert_hisq_data(row)
