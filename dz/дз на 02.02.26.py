
# books = [("Война и мир", 1865), ("1984", 1949), ("Гарри Поттер", 1997), ("Война и мир", 1865)]
# c = []
# c1 = []
# c2 = []
# c3 =[]
# for x,y in books:
#     if y > 1900:
#         c.append(x)
#     c1.append(y-100)
#
#     if y < 1950:
#         a = "классика"
#         c3.append(("классика"+x,y))
# print(c,c1,c3)
# Даны два кортежа a и b одинаковой длины.
# Сформируйте новый кортеж попарных сумм (a0+b0, a1+b1, ...) через цикл
# a = [1,2,3]
# b = [4,5,6]
# c = []
# for i in range(len(a)):
#     f = a[i]+b[i]
#     c.append(f)
# print(c)

# a = (1,2)
# b = (1,3)
# c=(*a,*b)
#
# s = {1,2,3,4,5}
# # v = set(range(1,6))
# # методы для всех множеств
# # sorted() reversed()
# # min max sum
# # in/not in
# # len
# # толькр для set
# set = {1,2,3}
# s.add(4)#  аналог append
# s.remove(4)#удалить
# s.discard(9)#не выводит ошибку если вызвать неправильный элемент
# s.clear()# очистка множества

# s = {1,2,3}
# s1 = {2,3,4}
# # объединение
# s2 = s.union(s1)#сохраняет в новое
# s.update(s1)#добавляет в иначальое множество
# # пересечение объектов
# s2=s.intersection(s1)
# s.intersection_update(s1)#обавляет в иначальое множество
# # разность
# s2=s.difference(s1)
# s.difference_update(s1)
# # симметрическая разность(убираются общие остаются ток уникальные)
# s2=s.symmetric_difference(s1)
# s.symmetric_difference_update(s1)
# s1 ^ s2 краткая запись
# # отношение между множествами
# small_set = {3,5,7}
# big_set = {1,3,5,7,9}
# # является ли подстрокой(порядок не важен)
# print(small_set.issubset(big_set))
# print(big_set.issubset(small_set))
# #надмножество
# print(big_set.issuperset(small_set))
# #
# a = {1,2,3,4}
# b = {3,4,5,6}
# # второй способ пересечения
# print(a & b)
# a.intersection_update(b)
# print(a)
# set1 = {1,2,3}
# set2 = {4,5,6}
# c = set1.union(set2)
# print(c)
# print(set1 | set2)#сокращ запись объединения
#
# a = {2,4}
# b ={1,2,3,4,5}
# print(a.issubset(b))
# i = a <= b #сокращенная запись issubset
a = input()
s = set(a)
print(s,len(s))
s = False
for i in range(len(a)):
    for y in range(i+1,len(a)):
        if a[i] == a[y]:
            s = True
if s == True:
    print("есть повтор")
else:
    print("нет повтор символов")
# a = input()
# s = set(a)
# # if len(a)<len(s):
#     print("символы повтор")
# # краткая запись дифференс
# s - s1



