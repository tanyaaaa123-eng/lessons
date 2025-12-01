# contrl c - копирование
# control v - вставить
# contrl / - комментарий
# control v - вставить
# control z - откатить изменения
# control y - вернуть изменения

print("Hello world")
name = "hello"
a=0
b=0
# возвращает память где переменная  хранится значение
a=b
print(id(a),id(b))
# int - целочисленный
# a=10
# print(type(a))
# str - символьный тип данys[
# a=""
# bool - логический тип данных
# a=True
# print(type(a))
# list - список элементов
# a=[1,"hello", True]
# print(type(a))
# float -  число с плавающей точкой
# a=1.5
# print(a,type(a))
# a=.5
# print(a,type(a))
# a = 5.
# print(a, type(a))
# dict - {key:value} - набор элементов ключ значение
# d ={"key":"value"," key2":"value2"}
# print(d["key"])
# set - набор уникальных элементов
a = {1,2,3,4,5,5,5,5}
print(a,type(a))
# tuple - кортеж (набор неизменяемых значений)
a = (1,2,3,4,5,6)
b = [1,2,3,4,5]
b[2] = 10
# a[2] = 10
print(b)
