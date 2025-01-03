import numpy as np
from math import *
from matplotlib import pyplot as plt


begin, end = [eval(i) for i in input("Podaj poczatek i koniec (oddzielone spacja): ").split()]
num = 1000

cmd = input()
exec(f"fx = lambda t: {cmd.split(';')[0]}")
exec(f"fy = lambda t: {cmd.split(';')[1]}")



t = np.linspace(begin, end, num)


x, y = [], []
for t1 in t:
    try:
        x1 = fx(t1)
        y1 = fy(t1)
    except:
        x1 = nan
        y1 = nan 

    x.append(x1)
    y.append(y1)
    


plt.plot(x, y)

path = input("podaj nazwę pliku: ")
if path:
    plt.savefig(path)
else:
    plt.show()