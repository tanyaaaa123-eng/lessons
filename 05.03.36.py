# with open("1716.txt",mode = 'r',encoding="utf-8") as f :
#     l = list(map(int,f))
# mn = 1000000
# for i in l:
#     if 10<=i<100 and mn>i:
#         mn = i
# for i in range(len(l)-1):
#     a1 = l[i]
#     a2 = l[i+1]
#     e = []
#     # 1 способ
#     # c = 0
#     # if 10<= a1 <100:
#     #     c+=1
#     # if 10<= a2 <100:
#     #     c+=1
#     # if c == 1:
#     # 2 споособ(исключающее или)
#     if (10<=a1<100) ^ (10<=a2<100):
#         if (a1+a2)%mn == 0:
#             e.append(a1+a2)
# print(len(e),max(e))

with open("1702.txt",mode="r",encoding="utf-8")as f:
    l = list(map(int,f))
maxx = -1000000
for i in l:
    if (100<=i<1000 and i %10 == 3) and maxx<i:
        maxx = i
e = []
for i in range(len(l)-2):
    a = l[i]
    b = l[i+1]
    c = l[i+2]
    count = 0
    if a%10==3 and 100<=abs(a)<1000:
        count+=1
    if b%10==3 and 100<=abs(b)<1000:
        count+=1
    if c%10==3 and 100<=abs(c)<1000:
        count+=1
    if count>=1 and (a+b+c)< maxx:
        e.append((a+b+c))
print(len(e),max(e))







