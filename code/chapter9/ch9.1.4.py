# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter9/ch9.1.4.py


a = (21, 32, 43, 45)

for item in a:
    print(item)

print('-----------')
for i, item in enumerate(a):
    print('{0} - {1}'.format(i, item))
