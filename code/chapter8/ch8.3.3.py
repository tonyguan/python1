# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter8/ch8.3.3.py

i = 0

while i * i < 10:
    i += 1
    # if i == 3:
    #     break
    print("{0} * {0} = {1}".format(i, i * i))
else:
    print('While Over!')

print('-------------')

for item in range(10):
    if item == 3:
        break
    print("Count is : {0}".format(item))
else:
    print('For Over!')
