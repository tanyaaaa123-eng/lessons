# txt
# путь до файла
# s = open("test.txt")
# print(list(s.read()))
# l = s.readline()
# while l:
#     print(l)
#     l=s.readline()
# print(s.readline())

# s.close()
# while open("test.txt") as f:
#     print(f.read())#получает все символы
#     print(f.read(10))#считает 10 символов
#     print(f.readline())#получает одну строку
#     print(f.readlines())#список строк
#     for i in f:
#         print(i)#выведет все строки
#
#
#
#     print(f.tell)#определяет где находмтся указаьель
#     s.seek(0)#перествляет указатель

# r - cчитывание файла.если нет то оштбка
# w - открывает файл для записи
with open("test2.txt",mode="w",encoding="utf-8") as f:
    f.write("примет мир")#символы(запись)
    f.writelines(["привет\n"])#список строк(запись)
#a - режим добавления
# x - открывает режим для записи при условии что файла не существыуеть(создает файл)
#rb ab wb xb - чтение\запись в бинарном режиме(видеофайлыю.изображения)
#r+
# r+ - и читается и записывается(файл существует и будет записан)
# w+ - читается и записывается(файл создается если его нет и будет перезаписан)
#a+ - можем чиьтать до добавления новых файлов
#x+ - файл не дллжен существоаать
#with open("test3.txt",mode="w",encoding="uft-8")as d:
  #  d.writelines(["привет","мир","1"])
# with open("test3.txt",mode="r",encoding="uft-8")as g:
#     print(g)
#
# with open("test4.txt",mode="w",encoding="uft-8") as h:
#     for i in range(1,51):
#         h.write(str(i)+"\n")
# #with open("test4.txt",)

  #  h.writelines([input()])
#ith open("test.txt",mode="a",encoding="uft-8") as

#with open("test5.txt",mode="x",encoding="utf-8") as l:
   # l.write("первая\nВторая\n")
#with open("test5.txt",mode="r",encoding="utf-8")as d:
  # d.readline()
   # print(d.readline())

with open("903. txt", encoding="utf-8")
    as f:
    data = []
    for i in f:
        Line = list(map(int, i.split()))
    data.append(line)
    def f(
        f(Line): 1
        usage


    max_of_4 = max(line)
    min_of_4 = min(Line)
    sum_rest = sum(line) - max_of_4 - min_of_4
    return max_of_4 + min_of_4 <= sum_rest

count += 1
print (count))