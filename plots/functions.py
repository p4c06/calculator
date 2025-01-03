# encoding=utf-8
import numpy as np
from math import *
from matplotlib import pyplot as plt

maxx, minn = -1*inf, inf
num = 100
begin, end = 0, 10

colors = ["blue", "red", "green", "purple", "gray"]


begin, end = [eval(i) for i in input("Podaj poczatek i koniec (oddzielone spacja): ").split()]
cmd = input("Podaj funkcje (oddzielone srednikiem): ")

num = 10000
for (i, func) in enumerate(cmd.split(";")):

    exec(f"f = lambda x: {func}")

    x = np.linspace(begin, end, num)

    result = []
    for x1 in x:
        try:
            result.append(f(x1))
        except:
            result.append(nan)

    if (maxx == -1*inf):
        ax = plt.subplot()
        ax.set_xlim(left=begin, right=end)
        ax.set_ylim(min(result), max(result))

    maxx = max(maxx, max(result))
    minn = min(minn, min(result))


    

    plt.plot(x, result, color = colors[i%len(colors)])


    

    plt.plot([begin, end], [0, 0], color = 'black')
    plt.plot([0, 0], [min(result), max(result)], color = 'black')
    plt.grid(True)
    plt.title(cmd)

path = input("podaj sciezke pliku: ")
if path:
    plt.savefig(path)
else:
    plt.show()