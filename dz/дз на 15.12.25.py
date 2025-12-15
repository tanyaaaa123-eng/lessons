# 1
# Вычислите значение логического выражения:
# (x↔y)∨¬z , если x = ложь, y = ложь, z = истина.
x = False
y = False
z = True
l = (x==y) or not z
print(l)
# 2
# Вычислите значение логического выражения:
#  (x⊕y)∧z , если x = истина, y = ложь, z = истина.
x = True
y = False
z = True
print((x^y) and z)
# 3
# Вычислите значение логического выражения:
# (x↓y)∨¬z , если x = ложь, y = истина, z = истина.
x = False
y = True
z = True
l = not(x or y) or not z
print(l)
# 4.
# Вычислите значение логического выражения:
# (x≡y)∨((y∨z)→x) , если x = истина, y = ложь, z = ложь, w - истина.
x = True
y = False
z = False
w = True
l = (x==y) or (not(y or z) or x)
print(l)
# 5.
# Создайте переменную x = 25.
# Выведите значение x в двоичной, восьмеричной и шестнадцатеричной системах счисления.
x = 25
# print(bin(x))
print(format(x,"b"))
print(format(x,"o"))
print(format(x,"x"))

