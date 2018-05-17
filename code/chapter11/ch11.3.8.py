# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.3.8.py


class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

    # 类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    # 静态方法
    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)


interest1 = Account.interest_by(12_000.0)
print('计算利息：{0:.4f}'.format(interest1))
interest2 = Account.interest_with(12_000.0)
print('计算利息：{0:.4f}'.format(interest2))

