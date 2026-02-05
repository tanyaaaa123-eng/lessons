# словари
# a ={key:value}
# min max sum( и все методы только для ключей)
s = {"маша":10,"Петя": 21}
# # print(list(s))  (только ключи выведет)
# # print(list(s.items()))  (значение тоже выводет)
# for k,v in s.items():
#     print(k,v)
#
# print(list(s.keys()))#список ключей
# print(s.values())#список значений
# k = s.pop("маша")
# # pop("fbgt",10) удаление элемента
# # k = s.popitem() удалят последний элемент , возвращает (ключ и значение)
# s["настя"]= 30 добавим новый элемент
# s.update({"настя":10,"":}) расширям на неопред количетсво
# s.clear()
# s.setdefault("ht",10) возвращает значение и ставит новое если такого нет
# copy - создает копию
# s1=s.copy
# print(s1)
# n=dict.fromkeys((keys,""))

# получение значения (нет ошибки даже если нет ключа)
# l = s.get("маша")
# print(l,s)

# items values get update
# points = {"x":10}
# l =points.get("y")
# # if l == None:
# #     print(0)
# l = points.get("y",0)

# books = {"романы": 10,"детективы":5}
# books.update({"фантастика":8})
# print(books)

# a = {}
# b = input()
# h = b.split("")#попадет список
# for item in h:
#     key,value = item.split(":") #key,value = ["a",1]
#     s[key] = int(value)
# print(s)

# students = ["Анна",5,"Борис",4,"Вера",5]
# s= {}
# for i in range(0,len(students),2):
#     s[students[i]]= students[i+1]
#     key,value = students[i],students[i+1]
#
# a = input()
# b = set(a)
# l = {}
# for i in b:
#     l[i]=a.count(i)
# print(l)
