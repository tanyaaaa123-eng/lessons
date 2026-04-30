# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
# print(fact(10))
# F = F(n-1) + F(n-2)
# def fib(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2) + fib(n-3)
# print(fib(10))
# def f(n,y):
#     if n==y:
#         return 1
#     elif n>y or n == 11:
#         return 0
#     else:
#         return f(n+10,y)+ f(n*2,y) + f(n**2,y)
#
# print(f(2,20))
def f(n,y):
    if n==y:
        return 1
    elif n==9 or n==16 or y>n:
        return 0
    else:
        return f(n-1,y) + f(n-2,y) + f(n//3,y)
print(f(19,3))

