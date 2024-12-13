import numpy as np
from math import *
from matplotlib import pyplot as plt
from itertools import product

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True



begin, end, num = [int(i) for i in input().split()]
while True:
    cmd = input(">")
    exec(f"f = lambda x, y: {cmd}")

    x = np.linspace(begin, end, num)
   
    matrix = []
    
    for i in x:
        row  = []
        for j in x:
            row.append(f(i, j))
        matrix.append(row)
       
    
    plt.imshow(matrix, cmap = "Blues")
    plt.show()
        
