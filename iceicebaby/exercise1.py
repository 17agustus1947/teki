from numpy import *
from math import *

def f(n, x):
    result = 0.0
    for i in range(n):
        result = result + (((-1)**i)*(x**(2*i+1)))/(2*i+1)
    return result

x = math.pi/3
arc = arctan(x)
list_n = [3,5,10,20]

for i in list_n:
    print(arc)
    print(f(i, x))
    print(abs(f(i, x)-arc))
