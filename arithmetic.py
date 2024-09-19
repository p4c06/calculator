from math import *
from numpy import *

operation = input("> ")

while operation != 'quit':
    try:
        print(eval(operation))
    except Exception as e:              
        print(e)    
    operation = input("> ")