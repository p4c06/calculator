import numpy as np
from math import *
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True



begin, end, num = [int(i) for i in input().split()]
while True:
    cmd = input(">")
    exec(f"f = lambda x: {cmd}")

    x = np.linspace(begin, end, num)
    
    result = [f(x1) for x1 in x]

    plt.plot(x, result, color='red')
    plt.grid(True)
    plt.title(cmd)
    plt.show()