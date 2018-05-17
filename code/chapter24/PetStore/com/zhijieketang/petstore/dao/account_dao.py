# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter24/PetStore/com/zhijieketang/petstore/dao/account_dao.py

"""用户管理DAO"""
from com.zhijieketang.petstore.dao.base_dao import BaseDao


class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findbyid(self, userid):
        account = None
        try:
            # 2. 创建游标对象
            with self.conn.cursor() as cursor:
                # 3. 执行SQL操作
                sql = 'select userid,password,email,name,addr,city,country,phone ' \
                      'from accounts where userid =%s'
                cursor.execute(sql, userid)
                # 4. 提取结果集
                row = cursor.fetchone()

                if row is not None:
                    account = {}
                    account['userid'] = row[0]
                    account['password'] = row[1]
                    account['email'] = row[2]
                    account['name'] = row[3]
                    account['addr'] = row[4]
                    account['city'] = row[5]
                    account['country'] = row[6]
                    account['phone'] = row[7]

                # with代码块结束 5. 关闭游标

        finally:
            # 6. 关闭数据连接
            self.close()

        return account
