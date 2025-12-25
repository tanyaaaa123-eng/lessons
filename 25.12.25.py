# a = True
# # print(123 if a else 345)
# while a:
#     print("+")
# num = 0
# i = True
# while i:
#     if num < 10:
#         num += 1
#         print(num)
#     else:
#         break
# print("программа завершена")
# num = 11
# while num > 0:
#     num -=1
#     if num % 2 !=0:
#         continue
#     else:
#         print(num)
# a = [1,2,3,4,5,6]
# i = 0
# while i < 5:
#     print(a[i])
#     i = i + 1
# a = int(input())
# i = 0
# count = 0
# if a != 0:
#     while a != 0:
#         b = a % 10
#         print("остаток:",b)
#         count += 1
#         a = a//10
#         print("оставшиеся цифры :",a)
# else:
#     count = 1
# print(count)
# a = int(input())
# summ = 0
# while a != 0:
#     b = a % 10
#     summ += b
#     a = a // 10
# print(summ)
# a = 0
# s = True
# while a <= 10 :
#     a = a + 1
#     b= a ** 2
#     if b >50:
#         s = False
#         break
#     print(a ** 2)
#     if s:
#         print("Все квадраты меньше 50")
# a = 5
# s = True
# while a<=15:
#     print(a)
#     a = a + 1
#     if a == 10:
#         s = False
#         break
# if s:
#     print("Цикл завершен")
n = int(input())
a = 0
while a < 10:
    a = a + 1
    print(n,"*",a,"=",n*a)
















