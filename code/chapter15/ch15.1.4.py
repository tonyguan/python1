# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter15/ch15.1.4.py

f_name = 'coco2dxcplus.jpg'

with open(f_name, 'rb') as f:
    b = f.read()
    print(type(b))
    copy_f_name = 'copy.jpg'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')
