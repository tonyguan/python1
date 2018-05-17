# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/16.4/ch16.4.2.py

import configparser

config = configparser.ConfigParser()  # 创建配置解析器对象

config.read('data/Setup.ini', encoding='utf-8')  # 读取并解析配置文件

print(config.sections())  # 返回所有的节

section1 = config['Startup']  # 返回Startup节
print(config.options('Startup'))

print(section1['RequireOS'])
print(section1['RequireIE'])

print(config['Product']['msi'])

print(config['Windows 2000']['MajorVersion'])  # 返回MajorVersion数据
print(config['Windows 2000']['ServicePackMajor'])

value = config.get('Windows 2000', 'MajorVersion')  # 返回MajorVersion数据
print(type(value))  # <class 'str'>

value = config.getint('Windows 2000', 'MajorVersion')  # 返回MajorVersion数据
print(type(value))  # <class 'int'>
