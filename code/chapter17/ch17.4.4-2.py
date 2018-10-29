# coding=utf-8
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
