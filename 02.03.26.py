with open("1719.txt") as f:
    data = list(map(int,f))
v= min(data)
c = 0
maxx= -10
emty = []
for i in range(len(data)-1):
    s1 = data[i]
    s2 = data[i+1]
    if s1 % 27 == v or s2 % 27 == v:
        emty.append(s1+s2)
        c+=1
        #сумма и максимум сравниваются
        maxx = max(maxx,s1+s2)
#два варианта
print(c,maxx)
print(len(emty),max(emty))
maxx = -100000
with open("1723.txt") as f:
    data = list(map(int,f))
for i in data:
    if i % 100 == 90:
        if i > maxx:
            maxx = i # maxx = max(maxx,i)
arr = []
for i in range(len(data)-2):
    s1 = data[i]
    s2 = data[i + 1]
    s3 = data[i+2]
    if len(str(s1)) == 4 or len(str(s2))==4 or len(str(s3))==4:
        if s1+s2+s3 > maxx:
            arr.append(s1+s2+s3)
print(len(arr),min(arr))






