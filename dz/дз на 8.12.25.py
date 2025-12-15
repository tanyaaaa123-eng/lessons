my_list = [1, 3, 'text', (5, 7, 9), 2.18]
# Выведите размер переменной my_list в байтах.
print(my_list.__sizeof__())
#  номер 2
student = {"Имя":"Иван","Фамилия":"Иванов","Возраст":"17","Класс":"11А"}
print(student)
# номер 3
my_tuple = (1, 2, 3, 4)
a=list(my_tuple)
print(id(my_tuple),id(a),sep = ";")
# номер 4
nums = [1, 2, 3, 4, 5]
s=set(nums)
print(nums.__sizeof__() , s.__sizeof__() , sep = "|")