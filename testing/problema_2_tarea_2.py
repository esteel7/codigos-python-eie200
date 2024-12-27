import numpy as np
import matplotlib.pyplot as plt

# Constantes del problema
g = 9.81  # Gravedad (m/s^2)
C = 0.55  # Coeficiente empírico
D_tanque = 3.0  # Diámetro del tanque (m)
R_tanque = D_tanque / 2  # Radio del tanque (m)
D_orificio = 0.03  # Diámetro del orificio (m)
A_orificio = np.pi * (D_orificio / 2)**2  # Área del orificio (m^2)

# Ecuación diferencial dH/dt con el área corregida para un tanque esférico
def dHdt(t, H):
    if H <= 0:
        return 0
    # Área de la sección transversal del tanque esférico en función de H
    A_tanque = np.pi * (2 * R_tanque * H - H**2)
    Q_out = C * A_orificio * np.sqrt(2 * g * H)  # Caudal de salida
    return -Q_out / A_tanque  # Tasa de cambio de la altura del líquido

# Método de Runge-Kutta de tercer orden (RK3)
def RK3(f, t0, H0, h, t_end):
    t_vals = [t0]
    H_vals = [H0]
    t = t0
    H = H0
    while t < t_end and H > 0:
        k1 = h * f(t, H)
        k2 = h * f(t + h/2, H + k1/2)
        k3 = h * f(t + h, H - k1 + 2*k2)
        # Corrección en la actualización de H
        H = H + (k1 + 4*k2 + k3) / 6
        t += h
        t_vals.append(t)
        H_vals.append(H)
    return np.array(t_vals), np.array(H_vals)

# Condiciones iniciales
H0 = 2.75  # Altura inicial del agua en el tanque (m)
t0 = 0  # Tiempo inicial (s)
h = 0.01  # Paso de tiempo (s)
t_end = 10000  # Tiempo final (s) - suficientemente grande para vaciar el tanque

# Resolver la ecuación diferencial con RK3
t_vals, H_vals = RK3(dHdt, t0, H0, h, t_end)

# Verificamos si el tanque se vacía durante la simulación
if np.any(H_vals <= 0):
    time_to_empty = t_vals[np.where(H_vals <= 0)[0][0]]
    print(f"Tiempo para que el tanque se vacíe: {time_to_empty:.2f} segundos")
else:
    print("El tanque no se vacía completamente en el tiempo simulado.")

# Gráfico de la altura del agua en el tanque en función del tiempo
plt.figure(figsize=(8,6))
plt.plot(t_vals, H_vals, label='Altura del líquido en el tanque (H)')
if np.any(H_vals <= 0):
    plt.axvline(x=time_to_empty, color='r', linestyle='--', label=f'Tiempo de vaciado: {time_to_empty:.2f} s')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura del líquido (m)')
plt.title('Altura del líquido en función del tiempo (Tanque esférico)')
plt.legend()
plt.grid(True)
plt.show()