from numpy import *
from math import *
import matplotlib.pyplot as plt

file = open("textfile.txt")
x = []
y = []
eksdee = []
akar = []

for i in range(0,5):
    line = file.readline()
    word = line.split(",")
    x.append(int(word[0]))
    y.append(int(word[1]))

file.close()
for k in range(0,5):
    eksdee.append(x[k]**3)
    akar.append(sqrt(x[k]+y[k]))
    print(str(x[k]) + str(y[k]) + str(eksdee[k]) + str(akar[k]))

