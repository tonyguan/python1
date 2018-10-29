# coding=utf-8
# 代码文件：chapter15/ch15.1.3.py

f_name = 'test.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    copy_f_name = 'copy.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')
