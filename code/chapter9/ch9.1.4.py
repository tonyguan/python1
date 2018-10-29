# coding=utf-8
# 代码文件：chapter9/ch9.1.4.py


a = (21, 32, 43, 45)

for item in a:
    print(item)

print('-----------')
for i, item in enumerate(a):
    print('{0} - {1}'.format(i, item))
