# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter8/ch8.2.2.py

print("----范围-------")
for num in range(1, 10):  # 使用范围
    print("{0} x {0} = {1}".format(num, num * num))

print("----字符串-------")
#  for语句
for item in 'Hello':
    print(item)

# 声明整数列表
numbers = [43, 32, 53, 54, 75, 7, 10]

print("----整数列表-------")

#  for语句
for item in numbers:
    print("Count is : {0}".format(item))
