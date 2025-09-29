import numpy as np
import matplotlib.pyplot as plt

# Definimos la función que representa la derivada dy/dt = f(t, y)
def dydt(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Definimos la solución exacta
def y_exacta(t):
    return (4 / 1.3) * (np.exp(0.8 * t) - np.exp(-0.5 * t)) + 2 * np.exp(-0.5 * t)

# Condiciones iniciales
t0 = 0
y0 = 2
h = 0.5
t_final = 4

# Inicializamos los valores de t y y
t = np.arange(t0, t_final + h, h)
y = np.zeros_like(t)
y[0] = y0

# Implementamos el método de Euler
for i in range(len(t)-1):
    y[i+1] = y[i] + dydt(t[i],y[i])* h

# Calculamos la solución exacta
t_exact = np.linspace(t0, t_final, 100)
y_ref = y_exacta(t_exact)

# Graficamos los resultados
plt.plot(t, y, 'bo-', label='Método de Euler')
plt.plot(t_exact, y_ref, 'r-', label='Solución Exacta')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación: Método de Euler vs. Solución Exacta')
plt.legend()
plt.grid(True)
plt.show()