# имя функции(агрументы)
# def a():
#     b = 10
#     for i in range:
#         for j in range:
# a()
# значение по умолчанию всегда после значения
# def funk(name,age = 10):
#     print("hello"+name,age)
# funk("таня")
# funk("МАША")
#
#
# def funk(**kwargs):
#     print(kwargs)
#
#
# def funk(a,d):
#     return a+d #возвращаем значение
# s = funk(1,3)# получаем значение
# print(s)
#
# def a():
#     global b # обращаеся к глобальной видимости
#     # локальная область видимости
#     b = 1
# b = 10
# # глобальная область видимости
# print(b)
#
# def a():
#     x = 10
#     def z():
#         nonlocal x
#         x = 100
#     z()
#     print(x)

# def c_f(c):
#     print( c *9 / 5+ 32)
# print(c_f(20))
def b_s(l,t):
    if t not in l:
        return -1
    a = l.index(t)
    return a
print(b_s([1,2,3,4,5],2))


