# coding=utf-8
# 代码文件：chapter21/ch21.3.1.py

import urllib.request

import os
import re

url = 'http://p.weather.com.cn/'


def findallimageurl(htmlstr):
    """从HTML代码中查找匹配的字符串"""

    # 定义正则表达式
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)


def getfilename(urlstr):
    """根据图片连接地址截取图片名"""

    pos = urlstr.rfind('/')
    return urlstr[pos + 1:]


# 分析获得的url列表
url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()

    url_list = findallimageurl(htmlstr)

for imagesrc in url_list:
    # 根据图片地址下载
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        # 过滤掉用小于100kb字节的图片
        if len(data) < 1024 * 100:
            continue

        # 创建download文件夹
        if not os.path.exists('download'):
            os.mkdir('download')

        # 获得图片文件名
        filename = getfilename(imagesrc)
        filename = 'download/' + filename
        # 保存图片到本地
        with open(filename, 'wb') as f:
            f.write(data)

    print('下载图片', filename)
