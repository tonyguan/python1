# coding=utf-8
# 代码文件：chapter17/ch17.4.4-1.py

import pymysql


# 查询最大用户Id
def read_max_userid():
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
                return row[0]

        # with代码块结束 5. 关闭游标

    finally:
        # 6. 关闭数据连接
        connection.close()


# 1. 建立数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345',
                             database='MyDB',
                             charset='utf8')

# 查询最大值
maxid = read_max_userid()

try:
    # 2. 创建游标对象
    with connection.cursor() as cursor:

        # 3. 执行SQL操作
        sql = 'insert into user (userid, name) values (%s,%s)'
        nextid = maxid + 1
        name = 'Tony' + str(nextid)
        affectedcount = cursor.execute(sql, (nextid, name))

        print('影响的数据行数：{0}'.format(affectedcount))
        # 4. 提交数据库事物
        connection.commit()

    # with代码块结束 5. 关闭游标

except pymysql.DatabaseError:
    # 4. 回滚数据库事物
    connection.rollback()
finally:
    # 6. 关闭数据连接
    connection.close()
