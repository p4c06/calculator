import numpy as np
from math import *
from matplotlib import pyplot as plt
from itertools import product

begin, end = [int(i) for i in input().split()]
num = 1000

cmd = input()
cmap = "viridis"

if "<" in cmd or ">" in cmd:
    exec(f"f = lambda x, y: {cmd}".replace("xy", "x*y"))
    cmap = "Blues"
elif "=" in cmd:
    a, b = cmd.split("=")
    exec(f"g = lambda x, y: {a}".replace("xy", "x*y"))
    exec(f"h = lambda x, y: {b}".replace("xy", "x*y"))
    exec(f"f = lambda x, y: 0.95 < abs({a} / {b}) < 1.05".replace("xy", "x*y"))
    cmap = "Blues"
else :
    exec(f"f = lambda x, y: {cmd}".replace("xy", "x*y"))


x = np.linspace(begin, end, num)
y = x
matrix = []

for i in x:
    row  = []
    for j in y:
        row.append(f(i, j))
    matrix.append(row)
    

path = input("podaj sciezke pliku: ")
if path:
    plt.imsave(path, matrix, cmap = cmap)