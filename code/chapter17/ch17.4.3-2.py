# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter17/ch17.4.3-2.py

import pymysql

# 1. 建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             database='MyDB',
                             charset='utf8')

try:
    # 2. 创建游标对象
    with connection.cursor() as cursor:

        # 3. 执行SQL操作
        sql = 'select max(userid) from user'
        cursor.execute(sql)

        # 4. 提取结果集
        row = cursor.fetchone()

        if row is not None:
            print('最大用户Id ：{0}'.format(row[0]))

    # with代码块结束 5. 关闭游标

finally:
    # 6. 关闭数据连接
    connection.close()
