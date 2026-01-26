# for i in [1,2,3,4]:
# a = [1,2,3]
# print(list(a.__iter__()))
# my_iter = iter(a) # ставим указатель  на начало списка(итерируемого об)
# print(next(my_iter))# переставляем указатель на след элемент
#
# n = [2,4,6,8,10]
# n = list(range(2,11,2))
# it = iter(n)
# s = 0
# for _ in range(len(n)):
#     s += next(it)
# print(s)
# len,in,not in,index
# конкатенация с помощью +
# print("n"+"a")

# методы list(cписка)
# a = [1,2,3]
# a.append(4)# замена конкатенции .добавляет элеммет в конец списка
# print(a)
# a.extend([4,5,6]) # добавляет последовательность в конец списка
# a.insert(0,10) #вставляет элемент перед индексом(index,object)
# a.remove(3) # удаляет указанный элемент из списка
# a.pop(0)#удаляет элемент по индексу
# a.index(3)#выведит индекс переданного элемента(можно указать промежуток)
# s = a.count(2) # кол во знач в списке
# b = a.copy()#чтобы при измении b не менялось а
# b[0]= 10
# a.clear()# очищает список
# a = [8,44,556,2,444]
# a.sort()#от меньшего к большему
# a.sort(reverse=True)# от большего
# a = ["a","d","r"]
# a.sort()# по алфавиту сортиуется
# a.reverse()#в обратном порядке
# s = reversed(a)
# b = sorted(a)
# a = [1,2,3]
# print(max(a))
# print(min)
# print(sum)
#
# a = []
# c = 1
# while c <= 5:
#     b =int(input())
#     c = c + 1
#     a.append(b)
# print(a)
# nums = [1,2,3,2,4,2,5]
# b = nums.index(2)
# print(nums.index(2,b+1))
nums = [2,5,6,3,7,9,1,4,3,2,5]
i = 0
while i<len(nums):
    if nums[i] % 2 == 0:
        nums.pop(i)
    else:
        i += 1
print(nums)
a = input().split(" ")
# for i in range(len(a)):
#     a[i] = int(a[i])
a = list(map(int,a) # примняем функцию к каждому элементу последовательности
