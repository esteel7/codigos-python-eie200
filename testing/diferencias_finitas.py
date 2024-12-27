import numpy as np

# Definir la función f(x) y su derivada exacta

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def derivada_exacta(x):
    return -0.4*x**3 - 0.45*x**2 -1.0*x - 0.25

# Definición de las funciones para calcular la derivada por diferencias finitas
def diferencia_hacia_adelante(f, x, h):
    return (f(x + h) - f(x)) / h

def diferencia_hacia_atras(f, x, h):
    return (f(x) - f(x - h)) / h

def diferencia_centrada(f, x, h):
    return (f(x + h) - f(x -h)) / (2*h)

# Definimos x y los valores de h

x = 0.5
valores_h = [0.5, 0.25, 0.125, 0.0625, 0.03125]

for h in valores_h:

    d1 = diferencia_hacia_adelante(f, x, h)
    d2 = diferencia_hacia_atras(f, x, h)
    d3 = diferencia_centrada(f, x, h)

    print(f"\nEstimación usando h = {h}")           
    print(f"Diferencia finita hacia adelante: {d1:.6f}")
    print(f"Diferencia finita hacia atrás: {d2:.6f}")
    print(f"Diferencia finita centrada: {d3:.6f}")

print(f"\nDerivada exacta evaluada en x = {x}: {derivada_exacta(x):.6f}\n")