# N = 10+ 17
# from math import log2,ceil
# a = 7564230
# b = 31 * 2 ** 20
# for s in range(1,100):
#     f = ceil(log2(N))
#     g = ceil((f * s)/8)
#     if g * a > b:
#         print(s)
#         break
# пирамидка дз
# H = int(input())
# for i in range(1,H + 1):
#     print(" "* (H - i), end="")
#     for j in range(1,i):
#         print(j,end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# a = str(input())
# s = 0
# for i in a:
#     if int(a) <= 5:
#         s += 1
#     print(s)
# # 2 cпособ
# while a:
#     if a % 10 <= 5:
#         s += 1
#         print(s)
#     a //= 10
    # cлед
a = 4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021+25**2022-4*5**2023-2024
s = 0
# в строчку не переводится
#
# while a:
#     if a % 10 > 8:
#         s +=1
#     a // 10
# print(s)
# 25 ричная система счисл
# a = 4*3125**2019+3*6252020-2*125**2021+25**2022-4*5**2023-2024
# s = 0
# while a:
#     if a % 25 > 10:
#         s = s + 1
#      a = a // 25
# print(s)
# a = 2 * 729 ** 2014+2*2432016-2*81*2018+2*27**2020-2*9**2022-2024
# s = 0
# while a:
#     if a % 27 > 9:
#         s = s + 1
#     a = a // 27
#print(s)
#
# a = 4*25**2025-2*5*2000+125**1011-3*5*100-660
# s = 0
# while a:
#     if a % 5 == 4:
#         s = s + 1
#     a = a // 5
# print(s)
#
# a = 1331**650-55*121**610+77*11**510-3*11**100-221
# s = 0
# while a:
#     if a % 11 == 10:
#         s = s + 1
#     a = a // 11
# print(s)
# 6
# n = int(input())
# b = ""
# if n == 0:
#     b = 0
# while n > 0:
#         b = str(n%6) + b
#         n = n // 6
# print(b)
a = 3**333+3**22-9*111-9
s = 0
while a :
    if a % 3 ==2:
        s = s + 1
    a = a // 3
print(s)


