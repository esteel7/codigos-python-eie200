import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Máximo valor de n
n_max = 10

# Definimos el dominio
x = np.linspace(0, 2*np.pi, 100)

# Evaluamos e imprimimos la funcion de referencia
y_ref = np.sin(x)
plt.plot(x,y_ref,'x')

# Se crea lista con sólo el primer elemento
legends = ["Referencia=sin(x)"]

# Se inicializa la serie y se evalúa iterativamente
serie = np.zeros_like(x)

for n in range(n_max):
  legends.append(f"n = {n}")
  serie+= ((-1)**n)*x**(2*n+1)/factorial(2*n+1)
  plt.plot(x,serie)

plt.axis([0, 2*np.pi, -1, 1])
plt.legend(legends)
plt.show()