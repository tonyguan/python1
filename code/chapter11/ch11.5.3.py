# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter11/ch11.5.3.py


class ParentClass1:
    def run(self):
        print('ParentClass1 run...')


class ParentClass2:
    def run(self):
        print('ParentClass2 run...')


class SubClass1(ParentClass1, ParentClass2):
    pass


class SubClass2(ParentClass2, ParentClass1):
    pass


class SubClass3(ParentClass1, ParentClass2):
    def run(self):
        print('SubClass3 run...')


sub1 = SubClass1()
sub1.run()

sub2 = SubClass2()
sub2.run()

sub3 = SubClass3()
sub3.run()
