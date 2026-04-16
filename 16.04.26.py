# a = all([True,True])
# print(a)
# a = any([True,False])#хотя бы одно удовлетворяет условию
# print(a)
# all(i for i in range(10) if i>0)
# all([i>0 for i in range(10)])#[false,true,true..,] потому что сравнение
# a = [1,2,3,4,5,6]
# b = any(i %2==0 for i in a)
# print(b)
# #
# n = [1,2,3,4,5,6,7]
# k = [i*2 for i in n]
# def double(num):
#     return num*2
# d = [double(i) for i in n]
# print(d)
# # lambda
# a = lambda x:x*2
# d = [a(i) for i in n]
# #
# a = lambda x:x*2 if x==10 else 0 if x==20
# add = lambda a,a1:a+a1
# print(add(3,5))
# #
# str_len= lambda strr:len(strr)
# print(str_len("Python"))
# # max,min,sorted
# w = ["шаг","в","будущее"]
# a=sorted(w,key=len)#по первой букве
# #
# nums = [14,5,23,42,31]
# s = sorted(nums,key = lambda x: x%10)
# students = [
#     ("Анна", 98),
#     ("Василий ", 77),
#     ("Мария ", 92),
#     ("Иван", 84),
#     ("Полина ", 85),
# ]
# a = sorted(students,key = lambda x:x[1])
# students = [
#     {"name": "Анна", "score": 98},
#     {"name": "Василий", "score": 77},
#     {"name": "Мария", "score": 92},
#     {"name": "Иван", "score": 84},
#     {"name": "Полина", "score": 85}]
# s = sorted(students,key=lambda x: x["score"])
# h = sorted(students,key=lambda x: -x["score"])# от большего
# d = ["hello","aaaaaaaaaa"]
# s = max(d,key=len)# min
# print(s)
# s = [1,2,3]
# s.sort()
# student = [("Анна", 16), ("Бронислав", 15), ("Федот", 18)]
# a = min(student,key = lambda x:x[1])
# print(a)
 # Напишите функцию calculator, которая принимает
# две лямбды (для сложения и вычитания) и два
# числа, затем применяет каждую лямбду к числам
# и возвращает список результатов. Создайте
# соответствующие лямбды и вызовите функцию
# для 10 и 4. Выведите результат.
# def calculator(h,b,c,d):
#     return h(c,d),b(c,d)
# h = lambda c,d:c+d
# b = lambda c,d:c-d
# print(calculator(h,b,10,4))


