# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter17/ch17.4.4-2.py

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
        sql = 'update user set name = %s where userid > %s'
        affectedcount = cursor.execute(sql, ('Tom', 2))

        print('影响的数据行数：{0}'.format(affectedcount))
        # 4. 提交数据库事物
        connection.commit()

    # with代码块结束 5. 关闭游标

except pymysql.DatabaseError as e:
    # 4. 回滚数据库事物
    connection.rollback()
    print(e)
finally:
    # 6. 关闭数据连接
    connection.close()
