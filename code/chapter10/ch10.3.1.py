# coding=utf-8
# 代码文件：chapter9/ch10.3.1.py

def show_info(sep=':', **info):
    """定义**可变参数函数"""
    print('-----info------')
    for key, value in info.items():
        print('{0} {2} {1}'.format(key, value, sep))
    return  # return None 或省略


result = show_info('->', name='Tony', age=18, sex=True)
print(result)  # 输出 None


def sum(*numbers, multiple=1):
    """定义*可变参数函数"""
    if len(numbers) == 0:
        return  # return None 或省略

    total = 0.0
    for number in numbers:
        total += number
    return total * multiple


print(sum(30.0, 80.0))  # 输出110.0
print(sum(multiple=2))  # 输出 None
