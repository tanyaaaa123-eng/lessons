
# math_students = {"Анна", "Борис", "Вера", "Глеб"}
# physics_students = {"Борис", "Вера", "Дмитрий", "Елена"}
# chemistry_students = {"Вера", "Глеб", "Дмитрий", "Жанна"}
# print(math_students & physics_students & chemistry_students)
# a= (math_students & physics_students)| (math_students & chemistry_students)
# h = math_students - a
# print(h)
# b = (math_students | physics_students) - chemistry_students
# print(b)
# Найдите:
# Студентов, изучающих все три предметаСтудентов, изучающих только математику
# Студентов, изучающих математику или физику, но не химию
#
# 2.
# my_set = set()
# a = 0
# while a <5:
#     c = int(input())
#     my_set.add(c)
#     a +=1
# print(my_set)
# s = 0
# for i in range(len(my_set)):
#     s+=1
# print(s)
# print(min(my_set))
# print(max(my_set))

# Создайте программу для работы с множеством:
# Начните с пустого множества my_set.
# В цикле 5 раз запрашивайте у пользователя число.
# Добавляйте каждое число в множество с помощью add().
# После окончания ввода выведите итоговое множество и количество его элементов.
# Найдите минимальное и максимальное значения в множестве.

# 3.
# Даны два списка
list1 = [1, 3, 5, 7, 9, 11, 13, 15]
list2 = [2, 3, 6, 7, 10, 11, 14, 15]
a = set(list1)
b = set(list2)
c = a & b
print(c)
n = a-b
print(n)
s = a.symmetric_difference(b)
print(s)
