# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/16.4/ch16.4.3.py

import configparser

config = configparser.ConfigParser()  # 创建配置解析器对象

config.read('data/Setup.ini', encoding='utf-8')  # 读取并解析配置文件

# 写入配置文件
config['Startup']['RequireMSI'] = '8.0'
config['Product']['RequireMSI'] = '4.0'

config.add_section('Section2')   #添加节
config.set('Section2', 'name', 'Mac')   #添加配置项

with open('data/Setup.ini', 'w') as fw:
    config.write(fw)
