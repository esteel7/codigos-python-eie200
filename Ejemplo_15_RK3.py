import numpy as np
import matplotlib.pyplot as plt
from src2.metodosRK import Euler, Ralston, RK3

# Función que representa la ecuación diferencial dy/dx = f(x, y)
def dydx(x,y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

# Solución exacta
def y_exacta(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1.0

# Definimos el paso
h = 0.5

# Condición inicial y(x = 0) = 1.0
y0 = 1.0

# Resolvemos la EDO
x_range = [0.0, 4.0]
x, y_euler = Euler(x_range, dydx, h, y0) # Primer orden
x, y_ralston = Ralston(x_range, dydx, h, y0) # Segundo orden
x, y_RK3 = RK3(x_range, dydx, h, y0) # Tercer orden

# Definimos la solución de referencia
y_ref = y_exacta(x)

# Graficamos las soluciones
plt.plot(x, y_euler)
plt.plot(x, y_ralston)
plt.plot(x, y_RK3)
plt.plot(x, y_ref)
plt.legend(["Euler", "Ralston", "RK3", "Referencia"])
plt.grid(True)
plt.show()