# coding=utf-8
# 代码文件：chapter22/PetStore/com/zhijieketang/petstore/dao/account_dao.py

"""商品管理DAO"""
from com.zhijieketang.petstore.dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        """查询所有商品信息"""

        products = []

        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn ' \
                      'from products'
                cursor.execute(sql)
                # 4. 提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
                # with代码块结束 5. 关闭游标
        finally:
            # 6. 关闭数据连接
            self.close()

        return products

    def findbycat(self, catname):
        """按照商品类别查询商品"""

        products = []
        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn ' \
                      'from products where category=%s'
                cursor.execute(sql, catname)
                # 4. 提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
                # with代码块结束 5. 关闭游标
        finally:
            # 6. 关闭数据连接
            self.close()

        return products


    def findbyid(self, productid):
        """按照商品id查询商品"""

        product = None
        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select productid,category,cname,ename,image,listprice,unitcost,descn' \
                      ' from products where productid=%s'
                cursor.execute(sql, productid)
                # 4. 提取结果集
                row = cursor.fetchone()

                if row is not None:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]

                # with代码块结束 5. 关闭游标

        finally:
            # 6. 关闭数据连接
            self.close()

        return product
