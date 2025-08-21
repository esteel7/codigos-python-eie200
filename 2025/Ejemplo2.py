import numpy as np
import matplotlib.pyplot as plt

# Definir las variables
g = 9.81
c = 1.0
m = 2.5
v0 = 0

# Definir el vector de tiempos
t = np.linspace(0, 10, 100)
#print(t)
#print(t.shape) investigar el comportamiento de shape

# Definir la función de velocidad
v = v0 * np.exp(-(c/m)*t) + (g * m /c) * (1 - np.exp(-(c/m)*t))

print(v)

fig = plt.plot(t,v)

plt.title("Gráfica de velocidad vs tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.grid(True)
plt.show()