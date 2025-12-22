#math case
# or
# a = 10
# match a:
#     case 11 | 19: # сравнение эквивалентность ==
#         print("это 11")
#     case 9:
#         print("это 9")
#     case _: # else
#         print("ничего")
# аналогия if else elif
# match a:
#     case(0,1):
#         print("КООРДИНАТ")
#     case (0,e):
#         print("координаты 0",e)
#     case(u,y):
#         print("это другое условие")
# a = 10
# # match a:
# #     case a if a >0:
# #         print("")
# #     case a if a < 0:
# #         print("")
# #     case _:
# #         print("")
# a = int(input())
# match a :
#     case 1:
#         print("понед")
#     case 2:
#         print("вторник")
#     case 3:
#         print("среда")
#     case 4:
#         print("четверг")
#     case 5:
#         print("пятница")
#     case 6:
#         print("суббота")
#     case 7:
#         print("воскресенье")
# a = int(input())
# match a:
#     case 1 | 3| 5| 7| 9| 11:
#         print("30 дней")
#     case 2:
#         print("28 дней")
#     case 4 | 6| 8| 10| 12:
#         print("31 день")
#     case _:
#         print("")
#
# b = int(input())
# a = input()
# match (a,b):
#      case ("рабочий",t) if 9<= t<= 18 :
#          print("")
#      case("вызодной",t) if 10<= t <= 16 :
#          print("")
# x = int(input())
# y = int(input())
# match (x,y):
#     case(r,u) if r > 0 and u > 0:
#         print("во второй четверти")
#     case(r,v) if r < 0 and v > 0:
#         print("в первой четверти")
#     case(r,w) if r > 0 and w <0:
#         print("в четвертой")
#     case(r,e) if r < 0 and e < 0:
#         print("в третьей")
#     case (0, 0):
#         print("начало кооринат")
#     case(0,f) :
#         print("на оси оу")
#     case(r,0) :
#         print("на оси ох")
# a = input()
# c = int(input())
# b = int(input())
# match (c,a,b):
#     case (d,"+",v):
#         print(c + b)
#     case(d,"*",v):
#         print(c * b)
#     case(d,"-",v):
#         print(c - b)
#     case(d,"/",v) if v !=0:
#         print(c / b)
# a = int(input())
# c = a % 10
# b = a // 10
# b = b % 10
# n = a // 100
# m = 0
# if c % 5 == 0 or c % 2 == 0:
#     m = m + 1
# if b % 5 == 0 or b % 2 == 0:
#     m = m + 1
# if n % 5 == 0 or n % 2 == 0:
#     m = m + 1
# if m >= 2:
#     print(a)
# else:
#     print(a+1)
#
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
if a != 0:
    d =b**2-4*a*c
    if d > 0:
        d = sqrt(d)
        x1 = (-b+d)/(2*a)
        x2 = (-b-d)/(2*a)
        print(x1,x2)
    if d < 0:
        print("")
    if d ==0:
        x = (-b)/(2*a)
        print(x)


















