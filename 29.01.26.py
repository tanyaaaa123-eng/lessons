# a = input().split(" ")
# num = list(map(int,a))
# s = []
# for i in num:
#     if int(i)not in s:
#         s.append(int(i))
# print(s)
# s = [1,1,2,3,3,4,5,4,3,5,2]
# for i in range(1,len(s)-1):
#     if s[i - 1]< s[i] > s[i + 1]:
#         print(i)
#         break
# s = int(input())
# list_nums = []
# for i in s:
#     list_nums.append(int(i))
# print(list_nums)
# while s:
#     a = s%10
#     nums.append(int(i))
#
# a = [14,2,72,93,45,28,13,99,27,36,19,59,15,74,71]
#
# maxx = max(a)
# minn = min(a)
# v = a.index(maxx)
# v1 = a.index(minn)
# print(a[min(maxx,minn) + 1 : max(maxx,minn)])
# if v>v1:
#     print(a[v1:v])
# if v1>v:
#     print(a[v:v1])

# tuple
# s = ([1,2,4,4],[1,2,4,4])
# s[0][0] = 100
# print(s)
# s = "n","w"
# print(s,type(s))
# * - все элементы
# s,*b,n=("vsc","dfdd","fwvf","edef")
# s = ("fgff","dvd")
# s1 = ("dsw",'wwww')
# print(*s)
# b = (*s,*s1)
# print(b)
# tuple_n = (1,(2,3,4),5)
# a,*b,c=tuple_n
# print()
# a,(b,*k),c = tuple_n
# s = [(1,2),(1,3),(3,4)]
# for i,j in s:
#     print(i,j)
# s = {1:4,1:2}
# n = [([1,2],3),["XY",6]]
# for i in n:
#     [x,y],z= i
#     print(x,y,z)
#
# a = ((1,2),(3,4),(5,6))
# for i in a:# for x,y in a:
#     x,y=i
#     print(x*y)
cart =[("яблоки", 100), ("хлеб", 50), ("молоко", 80), ("яблоки", 100)]
c = []
c2 = []
c3 = []
for x,y in cart:
    if y>70:
        c.append(x)
        print(c)
    c2.append(x,y * 2)
    c3.append(x,y/2)
c3 = list(set(c3))
# append split map sort



