# from math import log2,ceil
# i = ceil(log2(80))
# for L in range(0,1000):
#     I = ceil(L*i/8)
#     if nums * I > memory:#количество номеров на объем памяти
#         print(L)
#         break
# line = '10,2 14,6'
# line = line.replace(",",".")
# line = line.split()
# line = line[1:]
# line = list(map(float,line))
with open("920.txt",mode = "r",encoding="utf-8")as f:
    d = []
    for line in f:
        d.append(list(map(int,line.split())))
c=0
for l in d:
    a =list(reversed(sorted(l)))
    if a[0] >(a[1]+a[2]+a[3]) and  len(a)==len(set(a)):
        c+=1
print(c)


with open("1725.txt",mode = "r",encoding="utf-8")as f:
    l = list(map(int,f))
maxx= []
c = []
for a in l:
    if a%2==0:
        maxx.append(a)
d = max(maxx)
for i in range(len(l)-1):
    a1= l[i]
    a2 = l[i+1]
    if (a1+a2)==d:
        c.append(a1**2 + a2**2)
print(len(c),max(c))


with open("1726.txt",mode = "r",encoding="utf-8")as f:
    l = list(map(int,f))
c = []
for i in range(len(l)-1):
    a1 = l[i]
    a2 = l[i+1]
    if abs(a1)%5==0 and abs(a2)%5==0:
        c.append(a1+a2)
print(len(c),min(c))

