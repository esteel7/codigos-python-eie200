import numpy as np

# Definir la función f(x) y su derivada exacta f'(x)
def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def f_prime_exact(x):
    return -0.4*x**3 - 0.45*x**2 - 1.0*x - 0.25

# Definir las funciones para calcular la derivada usando diferencias finitas
def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def centered_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# Valor en el que se evalúa la derivada
x = 0.5

# Valores de h a usar
h_values = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

# Cálculo de las derivadas
for h in h_values:
    fwd_diff = forward_difference(f, x, h)
    bwd_diff = backward_difference(f, x, h)
    ctr_diff = centered_difference(f, x, h)
    
    # Imprimir resultados de las aproximaciones
    print(f"\nPara h = {h}:")
    print(f"Diferencia finita hacia adelante: {fwd_diff:.6f}")
    print(f"Diferencia finita hacia atrás: {bwd_diff:.6f}")
    print(f"Diferencia finita centrada: {ctr_diff:.6f}")

# Cálculo de la derivada exacta en x = 0.5
f_prime_exact_value = f_prime_exact(x)
print(f"\nDerivada exacta en x = {x}: {f_prime_exact_value:.6f}")
