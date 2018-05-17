# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter16/16.2/ch16.2.3.py

import xml.etree.ElementTree as ET

tree = ET.parse('data/Notes.xml')
root = tree.getroot()

node = root.find("./Note")  # 当前节点下的第一个Note子节点
print(node.tag, node.attrib)
node = root.find("./Note/CDate")  # Note子节点下的第一个CDate节点
print(node.text)
node = root.find("./Note/CDate/..")  # Note节点
print(node.tag, node.attrib)
node = root.find(".//CDate")  # 当前节点查找所有后代节点中第一个CDate节点
print(node.text)

node = root.find("./Note[@id]")  # 具有id属性Note节点
print(node.tag, node.attrib)

node = root.find("./Note[@id='2']")  # id属性等于'2'的Note节点
print(node.tag, node.attrib)

node = root.find("./Note[2]")  # 第二个Note节点
print(node.tag, node.attrib)

node = root.find("./Note[last()]")  # 最后一个Note节点
print(node.tag, node.attrib)

node = root.find("./Note[last()-2]")  # 倒数第三个Note节点
print(node.tag, node.attrib)
