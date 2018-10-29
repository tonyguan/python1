# coding=utf-8
# 代码文件：chapter22/23.2/ch22.2.1.py

from db.db_access import findall_hisq_data


def main():
    """主函数"""
    data = findall_hisq_data('AAPL')

    print(data)


if __name__ == '__main__':
    main()
