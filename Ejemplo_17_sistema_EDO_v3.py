import numpy as np
import matplotlib.pyplot as plt

from src2.metodosRK_Sys import Euler, RK4

# Función que representa nuestra ecuación diferencial
# dy/dt = f(t, y)
def dydt(t, y, k=2*np.pi, m=1):

    dy1_dt = y[1]
    dy2_dt = -(k/m) * y[0]

    return np.array([dy1_dt, dy2_dt])

# Solución exacta de x(t)
def x_exacta(t, k = 2*np.pi, m = 1, x0 = 1, v0 = 0):
    omega = np.sqrt(k/m)
    return x0*np.cos(omega*t) + (v0/omega)*np.sin(omega*t)

def v_exacta(t, k = 2*np.pi, m = 1, x0 = 1, v0 = 0):
    omega = np.sqrt(k/m)
    return -x0*omega*np.sin(omega*t) + v0*np.cos(omega*t)

# Definimos el paso
h = 0.1

# Definimos la condición inicial y0 =[x(0), v(0)]
y0 = [1, 0]

#Definimos el rango de integración
t_range = [0.0, 4.0]

# Resolvemos el sistema de EDOs
t, y_euler = Euler(t_range, dydt, h, y0)
t, y_RK4 = RK4(t_range, dydt, h, y0)

x_ref = x_exacta(t)
v_ref = v_exacta(t)

fig, ax = plt.subplots(1,2)
ax[0].plot(t, y_euler[0,:])
ax[0].plot(t, y_RK4[0,:])
ax[0].plot(t, x_ref, 'x')
ax[0].title.set_text('Posición: x(t)')
ax[0].legend(['Euler', 'RK4','Referencia'])

ax[1].plot(t, y_euler[1,:])
ax[1].plot(t, y_RK4[1,:])
ax[1].plot(t, v_ref, 'x')
ax[1].title.set_text('Velocidad: v(t)')
ax[1].legend(['Euler', 'RK4', 'Referencia'])
plt.show()