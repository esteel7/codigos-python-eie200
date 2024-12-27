import numpy as np
import matplotlib.pyplot as plt
from src.funciones import factorial

# Definimos el dominio
x = 0.5

# Evaluar la funcion de referencia
y_ref = np.exp(x)

# Máximo valor de n
n_max = 10

# Criterio de parada
Ns = 6 # numero de cifras significativas
eps_s = 0.5*10**(2-Ns)

# Error actual
eps_a = 1e+10

# Evaluamos la serie
serie_prev = 1.0
serie_actual = 1.0
n = 1
print('\n Terminos   Resultado   error real (%)   error aproximado (%)')
while eps_a > eps_s:

  # Calculamos la serie
  serie_actual = serie_actual + x**n/factorial(n)

  # Recalculamos el error
  error_real = serie_actual - serie_prev
  eps_a = 100*(serie_actual - serie_prev)/serie_actual

  # Imprimimos el error
  print(' {}         {:.8f}     {:.5f}         {:.5f}'.format(n+1, serie_actual, error_real, eps_a))

  # Actualizamos el valor de n
  n = n + 1

  # Actualizamos el valor previo
  serie_prev = serie_actual

print(y_ref)