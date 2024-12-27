import numpy as np
import matplotlib.pyplot as plt

# Definimos la función dy/dt
def dydt(t, y):
    return 4*np.exp(0.8*t) - 0.5*y

# Solución exacta
def y_exacta(t):
    return (4/1.3) * (np.exp(0.8*t) - np.exp(-0.5*t)) + 2*np.exp(-0.5*t)

# Método RK4
def RK4(t0, y0, t_final, h):
    # Definimos el número de pasos
    N = int((t_final - t0)/h)
    
    # Inicializamos los arrays de t y y
    t = np.zeros(N+1)
    y = np.zeros(N+1)
    
    # Condiciones iniciales
    t[0] = t0
    y[0] = y0
    
    # Iteramos usando el método RK4
    for i in range(N):
        k1 = dydt(t[i], y[i])
        k2 = dydt(t[i] + h/2, y[i] + h/2 * k1)
        k3 = dydt(t[i] + h/2, y[i] + h/2 * k2)
        k4 = dydt(t[i] + h, y[i] + h * k3)
        
        y[i+1] = y[i] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        t[i+1] = t[i] + h
    
    return t, y

# Parámetros del problema
t0 = 0      # Tiempo inicial
y0 = 2      # Condición inicial y(0)
t_final = 2 # Tiempo final
h = 1       # Paso de integración

# Ejecutamos el método RK4
t_rk4, y_rk4 = RK4(t0, y0, t_final, h)

# Calculamos la solución exacta
t_exact = np.linspace(t0, t_final, 100)
y_exact = y_exacta(t_exact)

# Gráfica de la solución
plt.plot(t_rk4, y_rk4, 'bo-', label="RK4 (h=1)")
plt.plot(t_exact, y_exact, 'r-', label="Solución exacta")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Comparación del método RK4 con la solución exacta')
plt.grid(True)
plt.show()

# Imprimimos los resultados
print("Resultados del método RK4:")
for i in range(len(t_rk4)):
    print(f"t = {t_rk4[i]:.1f}, y = {y_rk4[i]:.5f}")