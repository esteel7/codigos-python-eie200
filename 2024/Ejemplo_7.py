import numpy as np
import matplotlib.pyplot as plt
from src.funciones import factorial

# Definimos el dominio
x = np.linspace(0, 2*np.pi, 100)

# Evaluar la funcion de referencia
y_ref = np.sin(x)

# Máximo valor de n
n_max = 10

# Lista vacia para las legendas
legends = []

# Evaluamos la serie
serie = np.zeros_like(x)
# serie = np.zeros(x.shape)
plt.figure(1)
plt.plot(x,y_ref,'x')
for n in range(n_max):
  legends.append('n = {:d}'.format(n))
  serie += (-1)**n*x**(2*n+1)/factorial(2*n+1)

  #serie = serie + (-1)**n*x**(2*n+1)/factorial(2*n+1)
  plt.plot(x,serie)

plt.axis([0, 2*np.pi, -1, 1])
plt.legend(legends)
plt.show()