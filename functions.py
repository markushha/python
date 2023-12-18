# functions is functions
import math

def pow(x, pow):
    return math.pow(x, pow)

def nroot(x, n):
    return math.pow(x, 1/n)

print(nroot(256, 4))