# Откройте файл 921.txt, содержащей в каждой строке четыре натуральных числа. Определите количество строк таблицы,
# содержащих числа, для которых выполнены оба условия:
# – среди четырёх чисел есть только одна пара равных чисел;
#
# – число, не являющееся ни максимальным, ни минимальным, больше 23.
#
# В ответе запишите только число.
with open("921.txt",mode="r",encoding="utf-8") as f:
    d =[]
    for line in f:
        l = list(map(int,line.split("\t")))
        d.append(l)
def r1(line):
    a = set(line)
    if len(line) - len(a) == 1:
        return True
def r2(line):
    b = line.copy()
    mx = (max(line))
    s1 = (min(line))
    c = 0
    for i in line:
        if i > 23 and i not in(mx,s1):
            return True
count = 0
for j in d:
    if r1(j) and r2(j):
        count+=1
print(count)
# Откройте файл 923.txt, содержащей в каждой строке восемь натуральных чисел. Определите количество строк таблицы,
# содержащих числа, для которых выполнены оба условия:
# – в строке есть одно число, которое повторяется трижды, есть другое число, которое повторяется дважды, остальные три числа различны;
#
# – среднее арифметическое неповторяющихся чисел строки не больше числа, повторяющегося трижды.
#
# В ответе запишите только число.
# with open("923.txt", mode= "r",encoding="utf-8") as f:
#     d = []
#     for line in f:
#         l = list(map(int,line.split("\t")))

#         d.append(l)
# def r1(line):
#     a = []
#     for i in set(line):
#         a.append(line.count(i))
#     a.sort()
#     if a == [1,1,1,2,3]:
#         return True
# def r2 (line):
#     sr = []
#     a = 0
#     for i in set(line):
#         if line.count(i) == 1:
#             sr.append(i)
#         if line.count(i) == 3:
#             a+= i
#         if sum(sr)/len(sr) <= a:
#             return True
# count = 0
# for line in d:
#     if r1(line) and r2(line):
#         count+=1
# print(count)
# Откройте файл 925.txt, содержащей вещественные числа
# — результаты ежечасного измерения концентрации примесей в воде очистных установок на протяжении трёх месяцев.
# Найдите процентное содержание значений концентраций, превышающих 9,0, среди значений концентраций
with open("925.txt",mode="r",encoding="utf-8") as f:
    f.readline()
    d = []
    for line in f:
        d.extend(list(map(float,line.replace(",","."), line.split()[1:])))
a = []
for i in d:
    if i > 9.0:
        a.append(i)
print((len(a)/len(d)) * 100)



