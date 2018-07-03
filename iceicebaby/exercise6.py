from numpy import *
from math import *
from sympy import *
import matplotlib.pyplot as plt

def f(n, x):
    result = 0.0
    for i in range(n):
        result = result + ((-1)**i)*(x**(2*i+1))/factorial(2*i + 1)
    return result

myList = [5,10,20,50,100]
x = math.pi/3
sin_x = sin(x)
error = []

for i in range (len(myList)):
    e = (abs(f(myList[i], x)-sin_x))
    print(e)
    error.append(e)

plt.plot(myList, error, label = "Relative Error")
plt.legend(loc = "best")
plt.show()
