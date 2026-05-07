def f(n,y):
    if n==y:
        return 1
    elif n > y or n==30 or n==18:
        return 0
    else:
        return f(n+1,y)+ f(n*3,y) + f(n*5,y)
print(f(2,90))
# 145
def f(n,y):
    if n==y:
        return 1
    elif n < y  :
        return 0
    else:
        return f(n-2,y)+ f(n//2,y)
print(f(32,1))
def f(n,y):
    if n==y:
        return 1
    elif n > y:
        return 0
    else:
        return f(n-1,y)+ f(n//2,y)
print(f(30,1))
