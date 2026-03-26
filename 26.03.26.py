# phone = "+7 (999) 123-45-67"
# phone = list(map(int,phone.replace("+","").replace("(","").replace(")","").split()[:2]))
# print(phone)
# log = "2023-10-25 [14:30:05] INFO: User logged in"
# line=log.split()[1]
# line = line.strip("[]")
# line = line.split(":")
# line = map(int,line)
# line = list(line)
# print(line)
# import string
# print(string.ascii_lowercase)#из таблицы аски нижнего регистра
# print(string.ascii_uppercase)#верхний регистр
# print(string.ascii_letters)#объединяет и верхн и нижний регистр
# print(string.digits)#все цифры 10 системы
# print(string.octdigits)# из восьмеричной
# print(string.hexdigits)# из 16-тиричной
# print(string.punctuation)# все символы
# print(string.printable)#все символы
# print(string.printable[:12]) #вск цифры 12 ричной системы
# print(string.whitespace)#все пробельные символы
# print(f"Нужно {s} рублей")
# import string
# for x in string.printable[:27]:
#     n = int(f"123{x}24",27)
#     n1 = int(f"135{x}78",27)
#     res = n1+n
#     if res%26==0:
#         print(res/26)
# s1,*s2,s3 = (11,12,13,14,15)
# s = [(1,2),(3,4),(5,6)]
# for i,j in s:
#     print(i,j)
#
# s = ["hello","world","my","name","is","tanya"]
# for i in range(len(s)):
#     print(f"{i} {s[i]}")
# for i,element in enumerate(s,start = 3):
#     print(f"{i} {element}")
# s = {"key1":"value1","key2":"value2"}
# for i,(key,value) in enumerate(s.items()):
#     print(f"{i} , {key}, {value}")
with open("901.txt")as f:
    d = []
    for line in f:
        a = list(map(int,(line.split())))
        d.append(a)
for i in d:
    b = []
    for j in i:
        b.append(i.count(j))
    b1 = sorted(b)
    if b1 ==[1,3,3,3,3,3,3]:
        return True
for i,line in enumerate(d,start=1):
    print(i)











