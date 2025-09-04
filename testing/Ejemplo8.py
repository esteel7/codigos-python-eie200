import numpy as np
import matplotlib.pyplot as plt

#Definir e inicializar los parámetros
m, g, c, v0 = 2.5, 9.81, 1.0, 0.0

t = np.linspace(0, 10, 100)
dt = t[1] - t[0]

v = np.zeros_like(t)
v[0] = v0

for i in range(1, t.size):
    v[i] = v[i-1] + (g - (c/m)*v[i-1]) * dt  # Euler explícito

print(f"Velocidad final ≈ {v[-1]:.6f} m/s")

plt.plot(t, v)
plt.grid(True)
plt.title("Gráfica de velocidad vs tiempo (m/s)")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.show()