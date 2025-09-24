import numpy as np

# ======================================================
# Sección 1: Ejemplo con números reales
# ======================================================

# Definición de variables
R1, R2, R3 = 220, 470, 560
V1, V2, Vj = 18, 9, 0.7

# Matriz de coeficientes
A = np.array([[R1+R2, -R2],[-R2, R2+R3]])

# Vector de términos independientes
b = np.array([Vj - V1, -V2])

# Resolver el sistema
x = np.linalg.solve(A, b)

i1, i2 = x

print(f"i1 = {i1:.5f} A e i2 = {i2:.5f} A")

# ======================================================
# Sección 2: Ejemplo con impedancias complejas
# ======================================================

# Definición de variables
Z1 = 10 + 5j
Z2 = 4 - 2j
Z3 = 8j
V1 = 12 + 3j
V2 = -6j
Vj = 1 + 0j

# Matriz de coeficientes
A = np.array([[Z1+Z2, -Z2],
              [-Z2, Z2+Z3]])

# Vector de fuentes
b = np.array([Vj - V1, -V2])

# Resolver
x = np.linalg.solve(A, b)
i1, i2 = x

print(f"i1 = {i1:.4f}, i2 = {i2:.4f}")


# ======================================================
# Sección 3: Ejemplo con fasores e impedancias complejas.
# ======================================================

# Parámetros
f = 60.0                      # Hz
w = 2*np.pi*f                 # rad/s
Vs = 120 * np.exp(1j*np.deg2rad(0))  # 120∠0° V (fasor)

R1 = 100.0        # ohm
L  = 0.2          # H
R2 = 150.0        # ohm
C  = 47e-6        # F
Zm = 50.0         # ohm (impedancia compartida)

# Impedancias complejas
Z1 = R1 + 1j*w*L
Z2 = R2 + 1/(1j*w*C)

# Matriz de coeficientes y vector de fuentes
A = np.array([[Z1 + Zm,     -Zm],
              [   -Zm,   Z2 + Zm]], dtype=complex)
b = np.array([Vs, 0], dtype=complex)

# Resolver mallas
I1, I2 = np.linalg.solve(A, b)

# Utilidades para mostrar en polar
to_polar = lambda z: (abs(z), np.rad2deg(np.angle(z)))

mag1, ang1 = to_polar(I1)
mag2, ang2 = to_polar(I2)

print(f"I1 = {I1:.4f} A  -> |I1|={mag1:.4f} A, ∠I1={ang1:.2f}°")
print(f"I2 = {I2:.4f} A  -> |I2|={mag2:.4f} A, ∠I2={ang2:.2f}°")

# Ejemplos de tensiones en componentes (fasores)
V_Zm = Zm*(I1 - I2)          # tensión en la impedancia compartida
V_R1 = R1*I1
V_L  = 1j*w*L*I1
V_R2 = R2*I2
V_C  = (1/(1j*w*C))*I2

magVm, angVm = to_polar(V_Zm)
print(f"V_Zm = {V_Zm:.2f} V -> |V_Zm|={magVm:.2f} V, ∠V_Zm={angVm:.2f}°")