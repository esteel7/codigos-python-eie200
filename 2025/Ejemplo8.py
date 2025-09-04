import numpy as np
import matplotlib.pyplot as plt

#Definir los parámetros
m, g, c, v0 = 2.5, 9.81, 1, 0

#Definimos el vector de tiempos t y dt=t[k+1]-t[k]
t = np.linspace(0,20, 100)
dt = t[1]-t[0]

# Inicializamos el vector de velocidades
v = np.zeros_like(t)
v[0]=v0

# Se itera para poblar el vector de velocidades
for i in range(1,t.size):
    v[i] = v[i-1] + (g - (c/m)*v[i-1])*dt

# Se imprime la velocidad final
print(f"Velocidad final: {v[-1]:.6f} m/s") #Se imprimen sólo 6 decimales de v[-1]

# Se grafican los datos
plt.plot(t,v)
plt.grid(True)
plt.title("Gráfica de velocidad vs tiempo (m/s)")
plt.xlabel("t")
plt.ylabel("v(t)")
plt.show()