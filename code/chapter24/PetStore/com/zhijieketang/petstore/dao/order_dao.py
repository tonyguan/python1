# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter24/PetStore/com/zhijieketang/petstore/dao/order_dao.py

"""订单管理DAO"""
import pymysql

from com.zhijieketang.petstore.dao.base_dao import BaseDao


class OrderDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        """查询所有订单"""

        orders = []
        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select orderid,userid,orderdate from orders'
                cursor.execute(sql)
                # 4. 提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    order = {}
                    order['orderid'] = row[0]
                    order['userid'] = row[1]
                    order['orderdate'] = row[2]
                    orders.append(order)
                # with代码块结束 5. 关闭游标
        finally:
            # 6. 关闭数据连接
            self.close()

        return orders

    def create(self, order):
        """创建订单，插入到数据库"""

        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'insert into orders (orderid,userid,orderdate,status,amount) ' \
                      'values (%s,%s,%s,%s,%s)'
                affectedcount = cursor.execute(sql, order)
                print('成功插入{0}条数据'.format(affectedcount))
                # 4. 提交数据库事物
                self.conn.commit()
                # with代码块结束 5. 关闭游标
        except pymysql.DatabaseError as e:
            # 4. 回滚数据库事物
            self.conn.rollback()
            print(e)
        finally:
            # 6. 关闭数据连接
            self.close()
