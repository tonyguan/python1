# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter23/23.2/ch23.2.1.py

from db.db_access import findall_hisq_data


def main():
    """主函数"""
    data = findall_hisq_data('AAPL')

    print(data)


if __name__ == '__main__':
    main()
