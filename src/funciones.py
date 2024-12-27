import numpy as np

def caida_libre(t,m,c,v0=0.0,g=9.81):
  '''
  Esta funcion calcula la velocidad de caida de un cuerpo.
  Los argumentos son:
    t: es vector de numpy (tiempo)
    m: punto flotante (masa)
    c: punto flotante (coeficiente de arrastre)
    v0: blabla (velocidad inicial)
    g: dsa (aceleracion de gravedad)

  Devuelve un arreglo de velocidades v
  '''
  # Evaluar la solucion
  v = v0*np.exp(-c/m*t) + g*m/c*(1 - np.exp(-c/m*t))
  return v

def factorial(n):
  if type(n) is int:
    if n == 0:
      fact = 1.0
    else:
      fact = 1.0
      for i in range(1,n+1):
        fact = fact*i
  else:
    fact = None
    print('No se puede calcular el factorial de un numero no-entero')
  return fact