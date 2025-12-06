import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1  # Masa
k = 1  # Constante del resorte
h = 0.1  # Paso de tiempo
t_final = 10  # Tiempo total

# Condiciones iniciales
x0 = 1  # Posición inicial
v0 = 0  # Velocidad inicial
a0 = -(k/m) * x0  # Aceleración inicial

# Inicialización de listas para guardar los resultados
t_vals = np.arange(0, t_final + h, h)
x_vals = [x0]
v_vals = [v0]
a_vals = [a0]

# Método de Newmark
for i in range(1, len(t_vals)):
    # Actualización de la posición
    x_new = x_vals[i-1] + h * v_vals[i-1] + (h**2 / 2) * a_vals[i-1]
    
    # Aceleración en el nuevo paso
    a_new = -(k/m) * x_new
    
    # Actualización de la velocidad
    v_new = v_vals[i-1] + h * (a_vals[i-1] + a_new) / 2
    
    # Guardar los nuevos valores
    x_vals.append(x_new)
    v_vals.append(v_new)
    a_vals.append(a_new)

# Solución teórica para comparación
def x_teorica(t):
    return x0 * np.cos(np.sqrt(k/m) * t)

x_teorica_vals = x_teorica(t_vals)

# Gráfico de los resultados
plt.figure(figsize=(10,6))
plt.plot(t_vals, x_vals, 'o-', label="Newmark")
plt.plot(t_vals, x_teorica_vals, 'r--', label="Solución teórica")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.title("Sistema Masa-Resorte usando el Método de Newmark")
plt.legend()
plt.grid(True)
plt.show()