import numpy as np
import matplotlib.pyplot as plt

# Constantes
Q = 1  # Carga total (usamos unidades arbitrarias)
epsilon_0 = 1  # Permisividad del vacío (usamos unidades arbitrarias)
a = 1  # Radio de la esfera (usamos unidades arbitrarias)

# Definir la función del campo eléctrico dentro y fuera de la esfera
def E_inside(r, Q, epsilon_0, a):
    return (Q / (4 * np.pi * epsilon_0 * a**3)) * r

def E_outside(r, Q, epsilon_0):
    return Q / (4 * np.pi * epsilon_0 * r**2)

# Rango de valores de r
r = np.linspace(0, 3*a, 500)

# Calcular el campo eléctrico
E = np.piecewise(r, [r <= a, r > a],
                 [lambda r: E_inside(r, Q, epsilon_0, a), 
                  lambda r: E_outside(r, Q, epsilon_0)])

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(r, E, label=r'$E(r)$', color='blue')

# Etiquetas y detalles
plt.title('Magnitud del Campo Eléctrico $E(r)$ de una Esfera Cargada Uniformemente')
plt.xlabel('Distancia $r$ desde el centro de la esfera')
plt.ylabel('Campo Eléctrico $E(r)$')
plt.axvline(x=a, color='red', linestyle='--', label=r'$r = a$')
plt.legend()
plt.grid(True)
plt.show()