import numpy as np
import matplotlib.pyplot as plt
from src2.metodosRK import Ralston, RK4

# Función que representa la ecuación diferencial dy/dx = f(x, y)
def dydt(t,y):
    return 4*np.exp(0.8*t) - 0.5*y

# Solución exacta
def y_exacta(t):
    return (4/1.3)*(np.exp(0.8*t) - np.exp(-0.5*t)) + 2*np.exp(-0.5*t)

# Definimos el paso
h = 1.0

# Condición inicial y(x = 0) = 1.0
y0 = 2.0

# Resolvemos la EDO
t_range = [0.0, 2.0]
#t, y_euler = Euler(t_range, dydt, h, y0) # Primer orden
t, y_ralston = Ralston(t_range, dydt, h, y0) # Segundo orden
t, y_RK4 = RK4(t_range, dydt, h, y0) # Cuarto orden

# Definimos la solución de referencia
y_ref = y_exacta(t)

# Graficamos las soluciones
#plt.plot(t, y_euler)
plt.plot(t, y_ralston)
plt.plot(t, y_RK4)
plt.plot(t, y_ref)
plt.legend(["Ralston", "RK4", "Referencia"])
plt.grid(True)
plt.show()