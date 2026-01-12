# i = 1
# while i < 6:
#     j = 0
#     while j < i :
#         print("*", end = "")
#         j +=1
#     print()
#     i += 1
#
# # None
# a = "hello"
# for i in a:
#     print(i)
# for i in range(0,100,10):
#     print(i)
# range(100) === range(0,100,1)
# for i in range(100,9,-10):
#     print(i)
# n = int(input())
# for i in range(1,10):
#     print(n,"*",i, "=", n * i)
# a = int(input())
# b = int(input())
# c = a
# while a <= b:
#     c = a * a
#     print(c)
#     a = a + 1
#
# a1 = (a-1)+(a-1)
# for i in range(0,)
# таблица умножения от 1 до N
# в формате j * i = k
N = int(input())
for i in range(1,N + 1):
    for j in range(1,N + 1):
        print(j,"*",i,"=",j * i)
# напишите программу которая использует вложенные циклы для вычисления квадратов чисел от А до В
# где A и В вводятся пользователем друг за другом(А <= В)
A = int(input())
B = int(input())
count = 0
for i in range(A,B + 1):
    k = i ** 2
    count = count + k
print(count)
# напишите программу вычисления N - го элемента ряда Фибоначчи
# числа фибоначчи - это ряд чисел, в котором каждое последующее число равно сумме двух предыдущих
N = int(input())
a = 0
b = 1
if N == 0:
     print(0)
elif N == 1:
     print(1)
else:
    for i in range(2,N + 1):
        a,b = a,b + b
        c = a
        a = b
        b = c + b
        print(b)
