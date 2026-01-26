# a = input()
# for i in a:
#     # является ли строка числоом мы проверяем наш символы по одлному
#     if i.isdigit():
#         print(a.upper())
# if " " in a:
#     print(a.replace(" ","*"))
# else:
#     print(a)
from operator import index

# a = input()
# s = "аоуеиыяэ"
# index = 0
# for i in range(len(a),-1,-1):
#     for a[i]in s:
#         index=i
#         break
# print(index,a[10])
# a = input()
# s = "АВЕКМНОРСТКУХ"
# v = 1
# f = "1234567890"
# if a[0] in s and a[4] in s and a[5] in s:
#     v = 1
# if a[1:4] is.digit:
#     v = v+1
# if v == 2:
#     print("True")
# else:
#     print("False")
# a = "1" * 81
# while "11111" in a or "88" in a:
#     if "11111" in a:
#         a = a.replace("11111","88",1)
#     else:
#         a = a.replace("888","8",1)
# print(a)
# a = "9"*100
# while "33333" in a or "999" in a:
#     if "33333" in a:
#         a = a.replace("33333","99",1)
#     else:
#         a = a.replace("999","3",1)
# print(a)
a = "1" + "0"*90
while "1" in a:
    if "10" in a:
        a = a.replace("10","0001",1)
    else:
        a = a.replace("1","000",1)
print(a.count("0"))
