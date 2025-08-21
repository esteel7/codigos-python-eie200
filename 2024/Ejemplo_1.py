# Este es un comentario

import numpy as np

import matplotlib.pyplot as plt

def Rx(tx):
    return np.array([[1, 0, 0],
                     [0, np.cos(tx), - np.sin(tx)],
                     [0, np.sin(tx), np.cos(tx)]])


print(Rx(0.1))