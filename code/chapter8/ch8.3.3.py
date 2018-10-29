# coding=utf-8
# 代码文件：chapter8/ch8.3.3.py

i = 0

while i * i < 10:
    i += 1
    # if i == 3:
    #     break
    print("{0} * {0} = {1}".format(i, i * i))
else:
    print('While Over!')

print('-------------')

for item in range(10):
    if item == 3:
        break
    print("Count is : {0}".format(item))
else:
    print('For Over!')
