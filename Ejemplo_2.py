import numpy as np
import matplotlib.pyplot as plt

# Definición de variables
g = 9.81
c = 1.0
m = 2.5
v0 = 0

t = np.linspace(0, 10, 100)

v = v0 * np.exp(-(c/m) * t) + (g * m /c) * (1 - np.exp(-(c/m)* t))

plt.plot(t, v)

plt.show()

