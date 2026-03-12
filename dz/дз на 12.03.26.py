# еализуйте метод isdigit().
# На вход поступает строка st (вводится пользователем).
# Необходимо определить, состоит ли строка только из цифр (символы от '0' до '9').
# Верните True или False. Реализовать при помощи цикла for или while на ваше усмотрение.
# При необходимости можно использовать функции len(), ord().
# Входные данные:
a = input()
def isdigit(a):
    c = 0
    for i in a:
        if 48<=ord(i)<=57:
            c+=1
    if c == len(a):
        return True
    else:
        return False
print(isdigit(a))
# pеализуйте метод isupper(). На вход поступает строка st (вводятся пользователем). Задача определить,
# все ли символы строки написаны в верхнем регистре.
# Верните True или False. Реализовать при помощи цикла for или while на ваше усмотрение.
a = input()
def issupper(a):
    c = 0
    for i in a:
        if 65<=ord(i)<=90:
            c+=1
    if c == len(a):
        return True
    else:
        return False
print(issupper(a))

