# coding=utf-8
# 代码文件：chapter7/7.4/hello.py

a = 0b10110010
b = 0b01011110

print("a | b = {0}".format(a | b))  # 0b11111110
print("a & b = {0}".format(a & b))  # 0b00010010
print("a ^ b = {0}".format(a ^ b))  # 0b11101100
print("~a = {0}".format(~a))        # -179
print("a >> 2 = {0}".format(a >> 2))  # 0b00101100
print("a << 2 = {0}".format(a << 2))  # 0b11001000

c = -0b1100
print("c >> 2 = {0}".format(c >> 2))  # -0b00000011
print("c <<  2 = {0}".format(c << 2))  # -0b00110000
