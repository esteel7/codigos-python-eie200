import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(t):
    return 15 - 12 * np.exp(-t / 0.015)

# Crear valores de t en un rango de 0 a 0.1 con pasos pequeños
t = np.linspace(0, 0.1, 1000)
# Evaluar la función en cada valor de t
y = f(t)

# Graficar
plt.plot(t, y, label=r'$f(t) = 15 - 12e^{-\frac{t}{0.015}}$')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Gráfica de $f(t) = 15 - 12e^{-t/0.015}$')
plt.legend()
plt.grid()
plt.show()