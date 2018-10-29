# coding=utf-8
# 代码文件：chapter15/ch15.1.4.py

f_name = 'coco2dxcplus.jpg'

with open(f_name, 'rb') as f:
    b = f.read()
    print(type(b))
    copy_f_name = 'copy.jpg'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')
