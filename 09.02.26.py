# a = input()
# a = a.upper()
# a = a.split(" ")
# s = {}
# for i in a:
#     for j in i:
#         if j in s:
#             s[j]+=1#изменеям значение по ключу
#         else:
#             s[j]=1# сохраняем новое значение по ключу


# a = a.replace(" ","")
# s = {}
# for j in set(a):#а не изменилось прсто перебираем уникальные
#     s[j] = a.count(j)
# print(s)
#
# a = input()
# a1 = input()
# b = a.split(" ")
# b1 = a1.split(" ")
# s = {}
# s1 = {}
# for i in b:
#     s[i]= b.count(i)
# for i in b1:
#     s1[i] = b1.count(i)
# m = s1.copy()
# for key,value in s.items():
#     if key in m:
#         m[key] += value
#     else:
#         m[key]=value
# print(m)
#
# m[key]=m.get(key,0)+value
#
#
# students = [
#     {'name': 'Alice', 'group': 'A', 'score': 85},
#     {'name': 'Bob', 'group': 'B', 'score': 92},
#     {'name': 'Charlie', 'group': 'A', 'score': 78},
#     {'name': 'David', 'group': 'C', 'score': 88},
#     {'name': 'Eve', 'group': 'B', 'score': 95}
# ]
# s = {}
# for i in students:
#     if i["group"] in s:
#         s[i["group"]].append(i["name"])
#     else:
#         s[i["group"]]=[i["name"]]
#
# print(s)

a = input()
b = a.split(" ")
s = {}
c= {}
for i in b:
    s[i]= a.count(i)
    print(a.count(i))
    if a.count(i)> 1:
        c[i]=a.count(i)
        b =list(sorted(c))
m = {}
for i in b:
    m[i]=c[i]
print(s)
print(c)
print(m)