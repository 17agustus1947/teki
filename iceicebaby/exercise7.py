import sympy as sym
import math

def f(x):
    return math.sin(x)/1+(x**2)

x = sym.symbols("x")
inter = sym.integrate(sym.sin(x)/1+x**2,x)
print("Calculate :" ,inter.subs(x, math.pi/2), "\"")

def simpson_13(a,b,n):
    h = (b-a)
    x = a
    s = 0

    for i in range(1,n):
        x = x + h
        if i % 2 == 0:
            k = 2
        else:
            k = 4
        s = s + k*f(x)
    return (b-a) * (f(a)+s+f(b))/(3*n)

n = [2,5,10,100]
a = 0
b = math.pi/2
exact = (float(inter.subs(x,b))) - (float(inter.subs(x,a)))
print(exact)
print("n \ Estimation \z Error")

for i in range(len(n)):
    print(str(n[i]), "\"" + str(simpson_13(a,b,n[i])), "\"" + str(100*abs(exact - simpson_13(a,b,n[i])/exact)))
