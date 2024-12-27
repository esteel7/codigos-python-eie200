import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(t, y) que representa la derivada dy/dt
def f(t, y):
    return 4 * np.exp(0.8 * t) - 0.5 * y

# Condiciones iniciales
t0 = 0
y0 = 2
h = 1.0
t_final = 4

# Inicializamos los valores de t e y
t = np.arange(t0, t_final + h, h)
y = np.zeros_like(t)
y[0] = y0

# Implementamos el método de Euler
for i in range(1, len(t)):
    y[i] = y[i-1] + h * f(t[i-1], y[i-1])

# Imprimimos los resultados
for i in range(1, len(t)):
    print(f"t = {t[i]:.1f}, y = {y[i]:.4f}")

# Graficamos los resultados
plt.plot(t, y, "bo-", label = "Método de Euler")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Método de Euler: dy/dt = 4e^{0.8t} - 0.5y")
plt.legend()
plt.grid(True)
plt.show()