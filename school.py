# 1
# from itertools import product, repeat
# p = product("дгиаше",repeat = 5)
# k = 1
# for x in p:
#     s = "".join(x)
#     if s[0] != "а" and s[0] != "и" and s[0] != "э" and s[4] != "г" and s[4] != "д" and s[4] != "ш":
#         print(k,s)
#         k += 1
#         print(k,s)
# # 2
# from itertools import product
# p = product("абдеоп",repeat = 6)
# k = 1
# for x in p:
#     s = "".join(x)
#     if s[0]=="о" and s.count("a")==1 and s.count("б")==1 and s.count("д")==1 and s.count("е")==1 and s.count("о")==1 and s.count("п")==1:
#         print(k,s)
#     k +=1
# #4
# from itertools import product
# p = product("масло",repeat = 6)
# for x in p:
#     s = "".join(x)
#     if s.count("с")==1 and s[0]!="а" and s[5]!="м" and s[5]!="л" and s[5]!="с" and s[0]!="о":
#         k +=1
#         print(k,s)
# for A in range(0,100):
#     if all(((2*x+y!=70)or(x<y)or(A<x)) for x in range(0,100) for y in range(0,100)):
#         print(A)
#файлы
# with open("17-1.txt",mode="r",encoding="utf-8") as f:
#     l = list(map(int,f))
#     c = []
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             a1 = l[i]
#             a2 = l[j]
#             if (a1+a2)%17==0:
#                 c.append(a1+a2)
# print(len(c),max(c))
# def staircase(n):
#     for i in range(1,n+1):
#         print("*" * i)
# n = int(input())
# staircase(n)
def triangle_type(a, b, c):
    n = []
    n.append(a)
    n.append(b)
    n.append(c)
    n1 = set(n)
    if len(n)==len(n1):
        print("Обычный треугольник")
    if len(n)-len(n1)==1:
        print("Равнобедренный треугольник")
    if len(n)-len(n1)==2:
        print("Равносторонний треугольник")
a = int(input())
b = int(input())
c = int(input())
triangle_type(a, b, c)
