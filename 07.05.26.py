# Алгоритм вычисления значения функции  F(n) , где
# n  – целое число, задан следующими соотношениями:
# F(n)=n  при  n<10 ;
#
# F(n)=3×n+F(n−3) , если  n≥10
#
# Чему равно значение выражения
# (F(6250)+2×F(6244))/F(6238) ?
# from functools import lru_cache
# @lru_cache()
# def f(n):
#     if n < 10 :
#         return n
#     if n>=10:
#         return 3*n+f(n-3)
# for n in range(1,6250):
#     f(n)
# print((f(6250)+2 * f(6244))//f(6238))
 # Алгоритм вычисления значения функции  F(n) , где  n  – целое число, задан следующими соотношениями:
# F(n)=n  при  n<20 ;
#
# F(n)=(n−6)×F(n−7) , если  n≥20
#
# Чему равно значение выражения  (F(47872)−290×F(47865))/F(47858)
from functools import lru_cache
@lru_cache()
def f(n):
    if n<20:
        return n
    if n>=20:
        return (n-6)*f(n-7)
for n in range(1,47872):
    f(n)
print((f(47872)- 290*f(47865))//f(47858))
# Исполнитель преобразует число на экране. У исполнителя есть две команды, которые
# обозначены латинскими буквами:
# A. Прибавить 1
#
# B. Прибавить 2
#
# C. Умножить на 2
#
# Сколько существует программ, которые преобразуют исходное число 4 в число 15, и
# при этом траектория вычислений программы содержит числа 11 и 13? Траектория
# должна содержать оба указанных числа.
# def f(x,y):
#     if x==y:
#         return 1
#     elif x>y:
#         return 0
#     else:
#         return f(x+1,y)+f(x+2,y)+f(x*2,y)
# print(f(4,11)*f(11,13)*f(13,15))
# def f(x,y):
#     if x==y:
#         return 1
#     elif x>y or x==10:
#         return 0
#     else:
#         return f(x+1,y)+f(x+2,y)+f(x*2,y)
# print(f(3,7)*f(7,20))
# from functools import lru_cache
# @lru_cache()
# def f(n):
#     if n<=5:
#         return 1
#     if n>5:
#         return n+f(n-2)
# for n in range(1,2126):
#     f(n)
# print(f(2126)-f(2122))
# def find(nimbers):
#     maxx = nimbers[0]
#     for i in nimbers:
#         if i>maxx:
#             maxx=i
#     return maxx
# def a(numbers):
#     for i in range(len(numbers)):
#         for j in range(i+1,numbers):
#             if numbers[i]==numbers[j]:
#                 return True
#     return False



