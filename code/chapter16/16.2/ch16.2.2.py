# coding=utf-8
# 代码文件：chapter16/16.2/ch16.2.2.py

import xml.etree.ElementTree as ET

tree = ET.parse('data/Notes.xml')  # 创建XML文档树
print(type(tree))  # xml.etree.ElementTree.ElementTree

root = tree.getroot()  # root是根元素
print(type(root))  # xml.etree.ElementTree.Element
print(root.tag)  # Notes

for index, child in enumerate(root):
    print('第{0}个{1}元素，属性：{2}'.format(index, child.tag, child.attrib))
    for i, child_child in enumerate(child):
        print('    标签：{0}，内容：{1}'.format(child_child.tag, child_child.text))
