import numpy as np
import matplotlib.pyplot as plt

# Función de ejemplo con cambios rápidos y lentos
def dydt(t, y):
    return np.sin(t) + 5*np.exp(-t)  # Cambios rápidos al principio, luego lentos

# Método de Euler adaptativo (simplificado)
def euler_adapt(t_range, y0, h0, tol):
    t_min, t_max = t_range
    t = [t_min]   # Lista para los tiempos
    y = [y0]      # Lista para las soluciones
    h = h0        # Paso inicial

    while t[-1] < t_max:
        # Evaluar la función en el punto actual
        dy = dydt(t[-1], y[-1])

        # Predicción usando el paso actual
        y_pred = y[-1] + h * dy

        # Predicción con un paso dividido (más preciso)
        h_half = h / 2
        y_half = y[-1] + h_half * dydt(t[-1], y[-1])
        y_half_pred = y_half + h_half * dydt(t[-1] + h_half, y_half)

        # Estimar error como la diferencia entre las dos aproximaciones
        error = np.abs(y_half_pred - y_pred)

        # Si el error es menor que la tolerancia, aceptamos el paso
        if error < tol:
            t.append(t[-1] + h)
            y.append(y_half_pred)

        # Ajustamos el tamaño del paso
        if error > 0:  # Evitar dividir entre 0
            h = h * min(2, max(0.1, 0.9 * (tol / error)**0.5))

    return np.array(t), np.array(y)

# Parámetros del problema
t_range = [0, 10]  # Rango de tiempo
y0 = 0             # Condición inicial
h0 = 1           # Paso inicial
tol = 1e-3         # Tolerancia

# Ejecutar el método
t_vals, y_vals = euler_adapt(t_range, y0, h0, tol)

# Gráfico de los resultados
plt.figure(figsize=(10,6))
plt.plot(t_vals, y_vals, '-o', label="Euler Adaptativo")
plt.xlabel('Tiempo (t)')
plt.ylabel('Solución (y)')
plt.title('Método de Euler Adaptativo')
plt.grid(True)
plt.legend()
plt.show()