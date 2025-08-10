import numpy as np
import matplotlib.pyplot as plt


# Definir el vector de tiempos
t = np.linspace(0.0, 10.0, 100)

def velocidad(t, m, c, v0 = 0, g = 9.81):

    # Evaluar la solucion
    v = v0*np.exp(-c/m*t) + g*m/c*(1 - np.exp(-c/m*t))

    return v

print(velocidad(t, 2.5, 1.0))