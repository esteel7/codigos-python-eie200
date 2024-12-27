import numpy as np
import matplotlib.pyplot as plt

from src2.metodosRK_Sys import Euler, RK4

# Función que representa nuestra ecuación diferencial
# dy/dt = f(t, y)
def dydt(t, y, k=2*np.pi, m=1):

    dx_dt = y[1]
    dv_dt = -(k/m) * y[0]

    return np.array([dx_dt, dv_dt])

def x_exacta(t, k = 2*np.pi, m = 1, x0 = 1, v0 = 0):
    omega = np.sqrt(k/m)
    return x0*np.cos(omega*t) + (v0/omega)*np.sin(omega*t)

# Definimos el paso
h = 0.1

# Definimos la condición inicial y0 =[x(0), v(0)]
y0 = [1, 0]

#Definimos el rango de integración
t_range = [0.0, 4.0]

# Resolvemos el sistema de EDOs
t, y_euler = Euler(t_range, dydt, h, y0)
t, y_RK4 = RK4(t_range, dydt, h, y0)

#print(t)
#print(y_euler)

plt.plot(t, y_euler[0])
plt.plot(t, y_RK4[0])
plt.plot(t, x_exacta(t))
plt.legend(["Euler", "RK4", "Referencia"])
plt.grid(True)
plt.show()