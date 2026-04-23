# Откройте файл 931.txt, содержащей в каждой строке четыре натуральных числа.
# Определите наибольший номер строки таблицы, для чисел которой выполнены оба условия:
# – наибольшее из четырёх чисел больше суммы трёх других;
# – все числа различны.
with open("931.txt")as f:
    d = []
    for line in f:
        a = list(map(int,line.split()))
        d.append(a)
#шаг 1
#print(d)
def r1(line):
    line.sort()
    #шаг 2
    # print(line)
    return line[3] >(line[0]+line[1]+line[2])
def r2(line):
    line2 = set(line)
    # шаг 3
    # print(line2)
    return len(line2)==len(line)
# for i,line in enumerate(d,start=1):
#     if r1(line) and r2(line):
        # print(i)
# ответ 24996
# Откройте файл 929.txt, содержащей в каждой строке семь натуральных чисел.
# Определите наименьший номер строки таблицы, для чисел которой выполнены оба условия:
# – в строке одно число повторяется четыре раза, остальные три различны;
#
# – сумма неповторяющихся чисел строки меньше суммы её повторяющихся чисел.
with open("929.txt")as f:
    d = []
    for line in f:
        a = list(map(int,line.split()))
        d.append(a)
#шаг 1
# print(d)
def r2(line):
    cc = []
    c = []
    for i in line:
        if line.count(i)>1:
            cc.append(i)
        elif line.count(i)==1:
            c.append(i)
    # шаг 2
    # print("непов",c,"повтор",cc)
    return sum(c)<sum(cc)
def r1(line):
    k = []
    for i in line:
        k.append(line.count(i))
    k.sort()
    # шаг 3
    # print(k)
    return k == [1,1,1,4,4,4,4]
for i,line in enumerate(d,start=1):
    if r1(line) and r2(line):
        print(i)
#ответ 6327


