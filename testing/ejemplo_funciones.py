import numpy as np

def f(x):
    return x**2+3*x + np.cos(x)

def derivada_exacta(x):
    return 2*x + 3 - np.sin(x)

print(derivada_exacta(3))