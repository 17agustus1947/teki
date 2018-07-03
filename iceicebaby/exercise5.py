from sympy import *

def f(x):
    return exp(1)**3*x + cos(x)

def simpson_13(a,b,n):
    h = (b-a)/n
    x = a
    fs = 0
    for i in range(1, n):
        x = x + h
        if i % 2 == 0:
            fs = fs + (2*f(x))

        else:
            fs = fs + (4*f(x))

    return (b-a)*(f(a)+fs+f(b))/(3*n)

n = 10
a = 0
b = pi/4

approx = simpson_13(a,b,n)

print(approx.evalf())




