def f(x,y):
    if x==y:
        return 1
    elif x>y or x==8:
        return 0
    else:
        return f(x+1,y)+f(x+2,y)+f(x*2,y)
print(f(3,14)*f(14,18))
#360
def f(x,y):
    if x==y:
        return 1
    elif x<y or x==7:
        return 0
    else:
        return f(x-1,y)+f(x-4,y)+f(x//3,y)
print(f(19,13)*f(13,2))
#68
from functools import lru_cache
@lru_cache()
def f(n):
    if n==1:
        return 1
    if n >1:
        return n*f(n-1)
for n in range(1,2024):
    f(n)
print((f(2024)//4+f(2023))//f(2022))
#1025661
from functools import lru_cache
@lru_cache()
def f(n):
    if n<=3:
        return n
    if n >3:
        return (n-2)*f(n-2)
for n in range(1,1024):
    f(n)
print((f(1024)+2*(f(1024)-f(1022)))//f(1020))
#3125280



