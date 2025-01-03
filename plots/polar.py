import numpy as np
from math import *
from matplotlib import pyplot as plt


begin, end = [eval(i) for i in input("Podaj poczatek i koniec (oddzielone spacja): ").split()]
num = 1000

cmd = input()
exec(f"f = lambda theta: {cmd}")

cmap = "Blues"

theta = np.linspace(begin, end, num)


r = []
for theta1 in angles:
    try:
        r1 = f(theta1)
    except:
        r1 = nan    

    r.append(r1)
    

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(theta, r)

path = input("podaj sciezke pliku: ")
if path:
    plt.savefig(path)
else:
    plt.show()