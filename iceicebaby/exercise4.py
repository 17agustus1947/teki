import matplotlib.pyplot as plt

def f(x):
    return 2*x**2+6*x+4

def diff3(x, h):
    return -3*f(x) - 4*(x+h) - f(x - 2*h)/float(2*h)

x=2
list_h=[0.01, 0.05, 0.1, 0.2, 0.5]
exact=[]
approx=[]
RealtiveError=[]

for i in list_h:
    exact.append(f(x))
    approx.append(diff3(x, i))

for k in range(0, 5):
    error = (100*abs(exact[k]-approx[k]/exact[k]))
    RealtiveError.append(error)
    print(str(exact[k]), str(approx[k]), str(RealtiveError[k]),"%")

plt.plot(list_h,RealtiveError,label="Realtive Error")
plt.legend(loc="best")
plt.show()
