import numpy as np
import matplotlib.pyplot as plt
from math import factorial

#Máximo valor de n
n_max = 10

#Definimos el vector x
x = np.linspace(0, 2*np.pi, 100)

#Definimos e imprimimos la función de referencia
y_ref = np.sin(x)
plt.plot(x,y_ref, 'x')

#Se crea una lista para las legendas y se agrega el primer elemento
legendas = ["Función referencia=sin(x)"]

#Inicializamos los valores de la serie
serie = np.zeros_like(x)

for n in range(n_max):
    legendas.append(f"n = {n}")
    serie += (((-1)**n)*(x**(2*n+1)))/factorial(2*n+1)
    #serie = serie + ((-1**n)*(x**(2*n+1)))/factorial(2*n+1)
    plt.plot(x,serie)

plt.axis([0, 2*np.pi,-1,1])
plt.legend(legendas)
plt.show()