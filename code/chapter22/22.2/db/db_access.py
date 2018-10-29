# coding=utf-8
# 代码文件：chapter23/23.2/db/db_access.py

import pymysql

def findall_hisq_data(symbol):
    """根据股票代码查询其股票历史数据"""

    # 1. 建立数据库连接
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='12345',
                                 database='nasdaq',
                                 charset='utf8')
    # 要返回的数据
    data = []

    try:
        # 2. 创建游标对象
        with connection.cursor() as cursor:

            # 3. 执行SQL操作
            sql = 'select HDate, Open, High, Low, Close, Volume,Symbol ' \
                  'from historicalquote where Symbol = %s '
            cursor.execute(sql, [symbol])

            # 4. 提取结果集
            result_set = cursor.fetchall()

            for row in result_set:
                fields = {}
                fields['Date'] = row[0]
                fields['Open'] = float(row[1])
                fields['High'] = float(row[2])
                fields['Low'] = float(row[3])
                fields['Close'] = float(row[4])
                fields['Volume'] = row[5]
                data.append(fields)

        # with代码块结束 5. 关闭游标
    except pymysql.DatabaseError as error:
        print('数据查询失败' + error)
    finally:
        # 6. 关闭数据连接
        connection.close()

    return data


def insert_hisq_data(row):
    """在股票历史价格表中传入数据"""

    # 1. 建立数据库连接
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='12345',
                                 database='nasdaq',
                                 charset='utf8')
    try:
        # 2. 创建游标对象
        with connection.cursor() as cursor:

            # 3. 执行SQL操作
            sql = 'insert into historicalquote ' \
                  '(HDate,Open,High,Low,Close,Volume,Symbol)' \
                  ' values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'

            affectedcount = cursor.execute(sql, row)
            print('影响的数据行数{0}'.format(affectedcount))
            # 4. 提交数据库事物
            connection.commit()

        # with代码块结束 5. 关闭游标
    except pymysql.DatabaseError as error:
        # 4. 回滚数据库事物
        connection.rollback()
        print('插入数据失败' + error)
    finally:
        # 6. 关闭数据连接
        connection.close()
