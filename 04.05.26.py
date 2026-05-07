import time
from turtledemo.penrose import start


# def f(x,y):
#     if x == y:
#         return 1
#     elif x<y:
#         return 0
#     else:
#         return f(x-2,y)+f(x//2,y)
# print(f(32,14 )* f (14,1))
# def f(x,y):
#     if x==y:
#         return 1
#     elif x<y:
#         return 0
#     else:
#         return f(x-1,y) + f(x//2,y)
# print(f(30,12) * f(12,1))
#O(1)- скорость вычислений не завивисит от данных
#i[0]
#O(log n) - количество элементов для обработки снимается вдвое при каждом шаге
#O(n) - время выполнения растет пропорционально количеству элементов
#for i in range():
# O(nlogn) - sorted (время растет но не в тааком количестве)
#O(n**2) - квадратичная сложность  - вложеные циклы
# O(2**n) - время удваивается с каждым новым элементом(рекурсия)
# fib_cache = {}
# def fib(n):
#     if n in fib_cache:
#         return fib_cache[n]
#     if n<2:
#         return n
#     resalt = fib(n-1) + fib(n-2)
#     fib_cache[n] = resalt
#     return resalt
# print(fib(5))
# from functools import lru_cache
# @lru_cache()
# #
# #(для функции будет работать каширование)
# #import time (замеряет время выполнения)
# #
# @lru_cache(maxsize=)
# #максимальное значение для кол ва кашшир объектов
# @lru_cache(typed=)
# #тип кешируемых результатов
# start = time.perf_counter()
# s = fn(100)
# end = time.perf_counter()
# print(f"{(end - start)* 10 ** 3:.3f}")
from functools import lru_cache
@lru_cache(maxsize=None)
# def F(n):
#     if n < 5:
#         return n
#     if n >=5:
#         return 2*n*F(n-4)
# for i in range(5,13767):
#     F(n)
# print(F(13766)-9*F(13762))/F(13758))
@lru_cache(maxsize=None)
def f(n):
    if n==1:
        return 1
    if n>1:
        return 2*n*f(n-1)
for n in range(1,2024):
    f(n)
print(f(2024)/16 - f(2023)/f(2022))





