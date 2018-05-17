# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter17/ch17.5.2.py

import dbm

with dbm.open('mydb', 'c') as db:
    db['name'] = 'tony'  # 更新数据
    print(db['name'].decode())  # 取出数据

    age = int(db.get('age', b'18').decode())  # 取出数据
    print(age)

    if 'age' in db:  # 判断是否存在age数据
        db['age'] = '20'  # 或者 b'20'

    del db['name']  # 删除name数据
