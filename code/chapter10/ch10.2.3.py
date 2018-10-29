# coding=utf-8
# 代码文件：chapter9/ch10.2.3.py


def sum(*numbers, multiple=1):
    """定义*可变参数函数"""
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple


print(sum(100.0, 20.0, 30.0))  # 输出150.0
print(sum(30.0, 80.0))  # 输出110.0
print(sum(30.0, 80.0, multiple=2))  # 输出220.0

double_tuple = (50.0, 60.0, 0.0)  # 元组或列表
print(sum(30.0, 80.0, *double_tuple))  # 输出220.0


def show_info(sep=':', **info):
    """定义**可变参数函数"""
    print('-----info------')
    for key, value in info.items():
        print('{0} {2} {1}'.format(key, value, sep))


show_info('->', name='Tony', age=18, sex=True)
show_info(sutdent_name='Tony', sutdent_no='1000', sep='-')

stu_dict = {'name': 'Tony', 'age': 18}  # 创建字典对象
show_info(**stu_dict, sex=True, sep='=')  # 传递字典stu_dict
