# x = True
# y = False
# z = False
# w = True
# l = (x==y)or(not(y or z) or x)
# print(l)
# #  импликация это <=
# a = 10
# b = 15
# c = 17
# a = a * (c-b)
# b = b ** 2
# c = (c % 3) + a
# r = c // b
# print(format(r,"o"))
# a = int(input())
# b = int(input())
# c = int(input())
# a = a ** 2
# b = b * c
# r = a + b
# print(format(r,"b"))
# a,b,c=7,14,21
# a = a * (c-b)
# b = b ** 2
# d = a + (c%5)
# d = d // b
# print(format(d,"b"))
# a = "1A"
# a=(int(a,16))
# d = "14"
# d= (int(d,8))
# x = (d - a) / 3
# print(x)
# a = "25"
# b = "17"
# a = int(a,16)
# b = int(b,8)
# x = (b - a)/5
# print(x)
# M = "2F"
# N = "36"
# O = 7
# M= int(M,16)
# N = int(N,8)
# M = M ** 2
# M = M // N
# M = M + O
# print(format(M,"b"))
import math
# a = 10
# b = 73
# print(math.ceil(b/a))
# import math
# a = 217
# print(math.floor(a/60))
# Фотограф делает цветные фотографии размером 3840х2160 пикселей,
v = 3840*2160*24
d = 16 * (2 ** 33)
a = d // v
b = 3742 % a
print(b)
