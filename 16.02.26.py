def is_prime(n:int):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(5))

def a(lst,target):
    if target not in lst:
        return -1
    s = lst.index(target)
    return s
print(a(sorted([4,5,2,6,8,1]),6))

def a(s,seperator ="_"):
    k = ""
    f = []
    for char in s:
        if char.isupper() and k :
            k += seperator + char
        else:
            k += char
        return k.lower()
print(a("ThehHhdhfJdnhdn"))
# Напишите функцию word_count(text, **kwargs),# которая принимает текст и именованные аргументы
# (например, ignore_case=True), и возвращает словарь с подсчетом слов
# (с учетом опций).
def a(text,**kwargs):
    s = text.split(" ")
    if kwargs.get("clear_text"):
        if type(text) == str:
            text = "".join(s[: -1])
        else:
            text = s[:-1]
    if kwargs.get("split_text"):
        text = s
    return text
print()

# def a(n):
#     v = []
#     for i in n:
#         if i not in v:
#             v.append(i)
#     return v
# a= input().split(" ")

# def a(*args):
#     return list(set(args))
# b= input().split(" ")
# print(a(*b))

def a(ope,*numbers,p = 2):
    if ope== "sum":
        return round((sum(numbers)),p)
    if ope == "max":
        return round((max(numbers)), p)
    if ope == "min":
        return round((min(numbers)), p)
    if ope == "multiple":
        k = 1
        for i in numbers:
            k*=i
        return round(k, p)
    if ope == "average":
        return round((sum(numbers)/len(numbers)), p)

print(a("sum",23456))
