# s = [int(i) for i in line]
# line = [122,1,222]
# s = [{i:item} for i,item in enumerate(line)]

# s = [i**2 for i in range(1,16)]
# print(s)
#
# print("идут доддт" if i == True else "дождя нет")
# s = [i for i in range(100) if i%2==0]
a = [12,5,8,130,44,17,23]
s = [i for i in a if i>10]
print(s)
a = ["aaa",",ggg"]
s = [i.upper() for i in a]
print(s)
a = []
for i in range(100):
    s=[]
    for j in range(10):
        s.append(1)
    a.append(s)
print(a)
n=int(input())

c = []
c1 = []
for i in range(n):
    a = input()
    b= int(input())
    c.append(a)
    c.append(b)
m = int(input())
for a,b in c:
    if b==m:
        c1.append(a)
print(c1)
n=int(input())
c = []
c1 = []
for i in range(n):
    a = input()
    b= int(input())
    c.append(a)
    c.append(b)
m = int(input())
с1 = [a for a,b in c if b==m]
print(c1)