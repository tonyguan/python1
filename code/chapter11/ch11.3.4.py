# coding=utf-8
# 代码文件：chapter11/ch11.3.4.py


class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额


account = Account('Tony', 1_800_000.0)

print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))

print('Account利率：{0}'.format(Account.interest_rate))
print('ac1利率：{0}'.format(account.interest_rate1))

print('ac1实例所有变量：{0}'.format(account.__dict__))
account.interest_rate = 0.01
account.interest_rate2 = 0.01
print('ac1实例所有变量：{0}'.format(account.__dict__))