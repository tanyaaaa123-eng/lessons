from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if  n==1:
        return 1
    if n > 1:
        return (n-1)*f(n-1)
for n in range(1,2024):
    f(n)
print((f(2024)+ 2*f(2023))/f(2022))

from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if  n<=3:
        return 1
    if n > 3:
        return (n+3)*f(n-2)
for n in range(1,2028):
    f(n)
print(f(2028)/f(2024))

from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if  n==1:
        return 2
    if n >= 2:
        return 3*f(n-1)-n
for n in range(1,2025):
    f(n)
print((f(2025)-f(2023)-1)//32022)

