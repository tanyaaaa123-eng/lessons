# import math
# N = 10+27
# i = math.log2(N)
# n = (12*2**10)//3548
# l = i * n
# print(l)
from math import log2,ceil
# m = 12*2**10
# for s in range(1,10):
#     bits = ceil(log2(37) )# бит
#     bytes = ceil(s * bits / 8 )# байт
#     print(bits,bytes)
#     if bits * 3548 >= m:
#         print(s)
#         break
N = 27
a = 7564230
b = 31*2**20
for s in range(1,100):
    f = ceil(log2(N))
    g = ceil(s*f/8)
    print(f,g)
    if a * f > b:
        print(s)
    break
