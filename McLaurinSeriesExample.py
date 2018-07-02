from numpy import *
from math import *

def fac(n, x):
    result = 0.0
    for i in range(n):
        result += x**2 + 2*1
        return result

x= math.pi/3
arc = arctan(x)
list = [2,4,6,8]

for i in list:
    print(arc)
    print(fac(i,x))
    print(abs(fac(i,x)-arc))