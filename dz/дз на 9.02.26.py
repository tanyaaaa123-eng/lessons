a = []
n = 40
for i in range(0,n):
    a.append(int(input()))
s = 0
x = 0
for i in range(n):
    if a[i]>0 and a[i]%a==0:
        s+=a[i]
        x+=1
if x>0:
    print(s/x)
else:
    print(0)
#2
a = []
n = 20
for i in range(0,n):
    a.append(int(input()))
m = 1001
for i in range(n):
    if a[i]%2 !=0 and a[i]%5 == 0:
        if a[i]<m:
            m = a[i]
print(m)
# 3
a = []
n = 30
for i in range(0,n):
    a.append(int(input()))
s = 0
for i in range(n):
    if a[i]%13==0:
        s+=a[i]
print(s)
