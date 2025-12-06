import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parámetros del problema RL
# -----------------------------
V0 = 10.0      # Voltios
omega = 50.0   # rad/s
R = 5.0        # Ohm
L0 = 0.2       # Henry
alpha = 0.1    # A^{-2}

t0 = 0.0       # tiempo inicial [s]
tf = 2.0       # tiempo final [s]
h = 0.001      # paso [s]
i0 = 0.0       # condición inicial i(0) [A]

# Cantidad de pasos
N = int((tf - t0) / h)

# Vectores para tiempo e i(t)
t = np.zeros(N + 1)
i = np.zeros(N + 1)

# Condiciones iniciales
t[0] = t0
i[0] = i0

# -----------------------------
# Definimos f(t,i) de la EDO
# -----------------------------
def f(t, i):
    """
    Ecuación diferencial:
    di/dt = ( V0*sin(omega*t) - R*i ) / ( L0*(1 + alpha*i^2) )
    """
    numerador = V0 * np.sin(omega * t) - R * i
    denominador = L0 * (1.0 + alpha * i**2)
    return numerador / denominador

# -----------------------------
# Bucle RK3 (implementación directa)
# -----------------------------
for n in range(N):
    t_n = t[n]
    i_n = i[n]

    # Paso 1: k1
    k1 = f(t_n, i_n)

    # Paso 2: k2
    k2 = f(t_n + 0.5*h, i_n + 0.5*k1*h)

    # Paso 3: k3
    k3 = f(t_n + h, i_n - k1*h + 2.0*k2*h)

    # Actualizamos i_{n+1}
    i[n+1] = i_n + (h/6.0) * (k1 + 4.0*k2 + k3)

    # Actualizamos tiempo
    t[n+1] = t_n + h

# -----------------------------
# Gráfico de i(t)
# -----------------------------
plt.figure()
plt.plot(t, i)
plt.xlabel("Tiempo t [s]")
plt.ylabel("Corriente i(t) [A]")
plt.title("Circuito RL no lineal - Método RK3")
plt.grid(True)
plt.tight_layout()
plt.show()
