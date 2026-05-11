from turtledemo.clock import setup


# def find(nimbers):
#     maxx = nimbers[0]
#     for i in nimbers:
#         if i>maxx:
#             maxx=i
# # линейная 0(n)
# #     return maxx
# def a(numbers):
#     for i in range(len(numbers)):
#         for j in range(i+1,numbers):
#             if numbers[i]==numbers[j]:
#                 return True
# # квадратичная
#     return False
# from time import asctime
# now = asctime()
# s = [1,2,3,4,4]
# print(find(s))
# end = asctime
# print(a(s))
# #
# import timeit
# time_res=timeit.timeit("sum(range(100))")
# print(time_res)
# timer = timeit.timeit(stmt="find(s)",setup="",number= 100,globals = globals())
# timer1 = timeit.timeit(stmt="a(s)",setup="",number= 100,globals = globals())
# print(timer,timer1)
# print(f"{timer:,6f}",f"{timer1:.6f}",f"{timer/timer1:.2f}")
# Дано отсортированное множество различных целых чисел и целевое значение.
# Нужно вернуть индекс, если цель найдена. Если нет,
# вернуть индекс, где бы он был, если бы был выставлен по порядку.
#
# Вам необходимо написать алгорим, обладающий O(log n) сложностью по время выполнения.
#
# В задании используется метод двух указателей.

# Ввод:
#
# nums = [1, 3, 5, 6]
# target = 5
# Вывод:
#
# 2
# Ввод:
#
# nums = [1, 3, 5, 6]
# target = 2
# Вывод:
#
# 1
# Ввод:
#
nums = [1, 3, 5, 6]
target = 7

from timeit import timeit
from random import randint
def s(nums,target):
#0(n)
  for i in range(len(nums)):
      if nums[i]==target:
          return i
  return 0
def s2(nums,target):
    l = 0
    r = len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m]==target:
            return m
        elif nums[m]<target:
            l = m+1
        else:
            r = m-1
    return 0


a=[i for i in range(1000000)]
timer = timeit("s(a,100000)",number=100,globals=globals())
print(timer)
# Дан массив положительных целых чисел nums и целое число target.
# Найдите самую короткую непрерывную подпоследовательность (подмассив),
# сумма элементов которой ≥ target, и верните её длину.
# Если такой подмассив не существует — верните 0.
# Требуемая сложность: O(n)
#
# Ввод:
# nums = [2,3,1,2,4,3]
# target = 7
#
# Вывод:
# 2
#
# Объяснение: подмассив [4,3] — самый короткий с суммой ≥ 7
# Ввод:
# nums = [1,4,4]
# target = 4
#
# Вывод:
# 1


