import numpy as np
import matplotlib.pyplot as plt

# Definir la función dydt
def dydt(t, y):
    return 4*np.exp(0.8*t) - 0.5*y

# Método RK4
def RK4_step(t, y, h, dydt):
    k1 = h * dydt(t, y)
    k2 = h * dydt(t + h/2, y + k1/2)
    k3 = h * dydt(t + h/2, y + k2/2)
    k4 = h * dydt(t + h, y + k3)
    return (k1 + 2*k2 + 2*k3 + k4) / 6

# Método RK4 Adaptativo
def RK4_adaptativo(dydt, t0, y0, h, t_end, tol):
    t = t0
    y = y0
    ys = [y0]
    ts = [t0]
    
    while t < t_end:
        if t + h > t_end:
            h = t_end - t
        
        # Un paso completo con paso h
        y_full = y + RK4_step(t, y, h, dydt)
        
        # Dos pasos con h/2
        y_half = y + RK4_step(t, y, h/2, dydt)
        t_half = t + h/2
        y_half = y_half + RK4_step(t_half, y_half, h/2, dydt)
        
        # Calcular error estimado
        error = np.abs(y_full - y_half)
        
        # Comparar el error con la tolerancia
        if error <= tol:
            # Si el error es aceptable, aceptar el paso completo
            t += h # t = t + h
            y = y_half
            ys.append(y)
            ts.append(t)
        else:
            # Si el error es muy grande, reducir el paso
            h /= 2
        
    return np.array(ts), np.array(ys)

# Parámetros del problema
t0 = 0
y0 = 2
h = 2
t_end = 2
tol = 1e-5

# Resolver usando el método RK4 adaptativo
t_values, y_values = RK4_adaptativo(dydt, t0, y0, h, t_end, tol)

# Solución exacta
def y_exacta(t):
    return (4/1.3)*(np.exp(0.8*t) - np.exp(-0.5*t)) + 2*np.exp(-0.5*t)

# Comparar con la solución exacta en t = 2
y_exact = y_exacta(t_end)
y_approx = y_values[-1]

print(f"Valor aproximado de y(2): {y_approx}")
print(f"Valor exacto de y(2): {y_exact}")
print(f"Error relativo: {np.abs(y_exact - y_approx) / y_exact * 100:.5f}%")

# Graficamos las soluciones
#plt.plot(t, y_euler)
plt.plot(t_values, y_values)
plt.plot(t_values, y_exacta(t_values))
plt.legend(["RK4 adap", "Referencia"])
plt.grid(True)
plt.show()