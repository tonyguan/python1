# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter4/4.5/com/pkg1/hello.py

import com.pkg2.hello as module1
from com.pkg2.hello import z

y = 20

print(y)  # 访问当前模块变量y
print(module1.y)  # 访问com.pkg2.hello模块变量y
print(z)  # 访问com.pkg2.hello模块变量z
