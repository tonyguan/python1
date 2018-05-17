# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter15/ch15.1.2.py

# 使用finally关闭文件
f_name = 'test.txt'
try:
    f = open(f_name)
except OSError as e:
    print('打开文件失败')
else:
    print('打开文件成功')
    try:
        content = f.read()
        print(content)
    except OSError as e:
        print('处理OSError异常')
    finally:
        f.close()

# 使用with as自动资源管理
with open(f_name, 'r') as f:
    content = f.read()
    print(content)

