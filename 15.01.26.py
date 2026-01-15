# a = (16 ** 350 * ((15*3-29)**(4**(2+5)))+ 1007 )//63
# s = ""
# while a:
#     s =str(a%4) + s
#     a = a//4
# print(s.count("1"))
# a = 14 ** 1402 + 28 ** 501 - 14** 51 - 1400
# c = 0
# while a:
#     if a % 14== 12:
#         c +=1
#     a //= 14
# print(c)
# print(ord("B"))
# print(ord("b"))
# word = "abc"
# for letter in word:
#     print(ord(letter))
# print("a"< "g")
# print(ord("a"),ord("g"))
# print(chr(35))
# word = "привет"
# print(word[-3])
# print="название- \"привет\"""
# # спеиальные символы
# \n
# # перенос строки
# \t
# # таб
# \r
# возрат каретки
# \b
# забой(backspace)
# x48 - H
# x69 - i
# вывод 16- значных символов \xxx
# print("\x48\x69")
# r - сырые строки
# срезы
# word = "Python"
# # print(word[2:])
# # print(word[1:4:2])
# # print(word[1:6:2])
# print(word[4:])
# # пропущена первая цифра то она считается за ноль
# print(word[:6])
# print(word[0:6])
# # если вторая цифра,то она считаетсяя за длину строки
# print(word[4:6])
# print(word[4:])
# # если пропущена третья цифра,то она считается за 1
# print(word[1:4:])
# print(word[1:4:1])
#
# print(word[-2:])
# word = "123456789"
# w = word[::2]
# print(w)
# w = word[1:-1]
# print(word[2:-2:2])
# # чтобы перевернуть
# print(word[::-1])
# s = int(input("введите строку"))
# print(s[:3])
# s = input("введите строку")
# print(s[-4:])
# s = input()
# # первые 5 и последние 5 выводит
# print(s[:5] + s[-5:])
# # первыу 5 в обратном порядке
# d = s[:5]
# print(d[::-1])
# s = input()
# if len(s) > 6:
#     print(s[2:6])
# else:
#     print(s)
#
# s = input()
# res = ""
# for i in range(len(s)):
#     if ( i + 1) % 3 != 0:
#         res += s[i]
# print(res)
# s = input()
# d = len(s)//2
# print(s[:d][::-1]+s[d:])
# s = input()
# for i in range(len(s)-2):
#     print(s[i:i+3])
# s = "шалаш,камыш,заказ,возврат,поиск,довод,спектр,комок,альянс"
# s =s.replace(" ","").split(",")
# print(s)
# for i in s:
#     if i[::-1] == i:
#         print(i)
# s = input("строка")
# a = int(input("сдвиг"))
# b = s[:a]
# v = s[a:] + b
# print(v)







