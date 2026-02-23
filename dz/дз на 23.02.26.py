# Откройте файл 902, содержащий в каждой строке четыре натуральных числа. Определите количество строк, содержащих числа,
# для которых выполнены оба условия:
# наибольшее из четырёх чисел меньше суммы трёх других;
# среди четырёх чисел есть только одна пара равных чисел.
# with open("902.txt",mode="r",encoding="utf-8") as f:
#     d =[]
#     for i in f:
#         l = list(map(int,i.split()))
#         d.append(l)
# def f(l):
#     m1 = max(l)
#     s = sum(l) - m1
#     return m1<s
# c = 0
# if len(d) - len(set(d))==1 and f(l):
#     c+=1
# print(c)
# # Откройте файл 905, содержащий в каждой строке шесть натуральных чисел. Определите количество строк,
# # содержащих числа,
# # для которых выполнены оба условия:
# # в строке только одно число повторяется трижды, остальные числа различны;
# # квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
# with open("905.txt",mode="r",encoding="utf-8") as f:
#     d = []
#     for i in f:
#         l = list(map(int, i.split("\t")))
#         d.append(l)
# def res1(i):
#     for x in i:
#         if i.count(x)== 3 and len(set(i))==4:
#             return True
# def res2(i):
#     s1 = 0
#     s2 = 0
#     for x in i :
#         if i.count(x)==1:
#             s1+= x
#         else:
#             s2 += x
# count = 0
# for i in d:
#     if res1(i) and res2(i):
#         count +=1
# print(count)


# a = set(d)
# c = list(a)
# h = d - a
# count = 0
# if len(d)-len(a)==3 and sum(a)**2> sum(h)**2:
#     c +=1
# print(c)


# Откройте файл 905, содержащий в каждой строке семь натуральных чисел. Определите количество строк, содержащих числа, для которых выполняются оба условия:
# в строке есть два числа, каждое из которых повторяется трижды, одно число без повторений;
# наибольшее из повторяющихся чисел больше неповторяющегося числа.

with open("907.txt",mode="r",encoding="utf-8") as f:
    d = []
    for i in f:
        l = list(map(int, i.split("\t")))
        d.append(l)
def a(i):
    s = 0
    for x in i:
        if i.count(x)==1:
            s += 1
    if s == len(i):
        return  True
def a2(i):
    s = sorted(i)
    return (s[3]+ s[4])<= (s[0]+s[1]+s[2])
count = 0

with open("908.txt",mode="r",encoding="utf-8") as f:
    d = []
    for line in f:
        l = list(map(int, line.split("\t")))
        d.append(l)
def a(line):
    s = sorted(line)
    maxx = s[3]
    if (sum(s[:3]) / s[3]) > 2:
        return True
def a2(line):
    for x in range(len(line)):
        for y in range(x+1,len(line)):
            s = line.copy()
            s.pop(y)
            s.pop(x)
            if line[x]+line[y]== sum(s):
                return True


with open("910.txt", mode="r", encoding="utf-8") as f:
        f.readline()
        s =[]
        for line in f:
            print(line)
            s.extend(list(map(float,line.replace(",",".").split()[1:])))
print(int(abs(min(s)-sum(s)/len(s))))
# abs - модуль



