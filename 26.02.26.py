# s1 = [6,19,1,14]
# s = [3,2,4,5]
# 1 способ
# n = s1[0]
# s1.remove(n)
# #s1.pop(0)
# for j in range(len(s1)):
#         a = s1.copy()
#         a.pop(j)
#         if n + s1[j]== sum(a):
#             print(True)
#             break
# s1 = [6,19,1,14]
# s = [3,2,4,5]
# a = [15,45,35,5]
# a.sort()
# if a[0]+a[3]==a[1]+a[2]:
#     print(True)
# with open("dz/908.txt",mode="r",encoding="utf-8") as f:
#     d = []
#     for line in f:
#         sp = line.split("\t")
#         l = list(map(int,line.split("\t")))
#         d.append(l)
#         # аналог map
#         # for i in sp:
#         #     s.append(int(i))
# def r1(line):
#     a = sorted(line)
#     maxx = a[3]
#     if (sum(a[:3]) / a[3]) >2:
#         return True
# def r2(line):
#     line.sort()
#     if line[0]+line[3]==line[1]+line[2]:
#         print(True)
# count = 0
# if r1(line) and r2(line):
#     count+=1
# print(c)
#
with open("922.txt",mode = "r",encoding="utf-8") as f:
    d = []
    for line in d:
        l = list(map(int,line.split("\t")))
        d.append(l)
def r1(line):
    emty = []
    for i in set(line):
        emty.append(line.count(i))
    emty.sort()
    if emty == [1,1,3,3]:
        return True
#
def r2(line):
    if line.count(max(line)) == 1:
        return True
c = 0
for list_line in d:
    if r1(list_line) and r2(list_line):
        c+=1
print(c)


