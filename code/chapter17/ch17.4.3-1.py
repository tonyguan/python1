# coding=utf-8
# 代码文件：chapter17/ch17.4.3-1.py

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
        # sql = 'select name, userid from user where userid >%s'
        # cursor.execute(sql, [0])
        sql = 'select name, userid from user where userid >%(id)s'
        cursor.execute(sql, {'id': 0})

        # 4. 提取结果集
        result_set = cursor.fetchall()

        for row in result_set:
            print('id：{0} - name：{1}'.format(row[1], row[0]))

    # with代码块结束 5. 关闭游标

finally:
    # 6. 关闭数据连接
    connection.close()
