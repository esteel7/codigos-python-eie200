import numpy as np
import matplotlib.pyplot as plt
from src.metodosRK import Euler, Heun

# Función que representa la ecuación diferencial dy/dx = f(x, y)
def dydx(x, y):
    return -2*x**3 + 12*x**2 - 20*x +8.5

# Solución exacta
def y_exacta(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1.0

# Definimos el paso h
h = 0.1

# Condición inicial y(x = 0) = 1.0
y0 = 1.0    

# Resolvemos la EDO
x_range = [0.0, 4.0]
x, y_euler = Euler(x_range, h, dydx, y0)
x, y_heun = Heun(x_range, h, dydx, y0)

# Definimos la solución de referencia
y_ref = y_exacta(x)

# Graficas las soluciones junto con la solución exacta
plt.plot(x, y_euler)
plt.plot(x, y_heun)
plt.plot(x, y_ref)
plt.legend(["Euler", "Heun", "Referencia"])
plt.grid(True)
plt.show()