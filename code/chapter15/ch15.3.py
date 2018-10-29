# coding=utf-8
# 代码文件：chapter15/ch15.3.py

import os.path
from datetime import datetime

f_name = 'test.txt'
af_name = r'C:/Users/win-mini/PycharmProjects/HelloProj/test.txt'

# 返回路径中基础名部分
basename = os.path.basename(af_name)
print(basename)  # test.txt

# 返回路径中目录部分
dirname = os.path.dirname(af_name)
print(dirname)

# 返回文件的绝对路径
print(os.path.abspath(f_name))

# 返回文件大小
print(os.path.getsize(f_name))  # 25
# 返回最近访问时间
atime = datetime.fromtimestamp(os.path.getatime(f_name))
print(atime)
# 返回创建时间
ctime = datetime.fromtimestamp(os.path.getctime(f_name))
print(ctime)
# 返回修改时间
mtime = datetime.fromtimestamp(os.path.getmtime(f_name))
print(mtime)

print(os.path.isfile(dirname))  # False
print(os.path.isdir(dirname))  # True
print(os.path.isfile(f_name))  # True
print(os.path.isdir(f_name))  # False
print(os.path.exists(f_name))  # True
