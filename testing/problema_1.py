import numpy as np

# Definición de variables
R1, R2, R3 = 220, 470, 560
V1, V2, Vj, Vz = 18, 9, 0.7, 3.9

# ======================================================
# Opción 1: Supuesto D1: ON y D2: ON
# ======================================================

# Matriz de coeficientes
A = np.array([[R1 + R2, -R2],[-R2, R2 + R3]])

# Vector de términos independientes
b = np.array([Vj - V1, V2])

# Resolver el sistema
x = np.linalg.solve(A, b)

i1, i2 = x

print(f"Supuesto D1: ON y D2: ON (CORRECTO)")
print(f"i1 = {i1:.6f} A e i2 = {i2:.6f} A")         # i1 = -0.027744 A e i2 = -0.003922 A
print(f"Id1 = {i2-i1:.6f} A e Id2 = {-i2:.6f} A")   # Id1 = 0.023822 A e Id2 = 0.003922 A
print(f"Vo = {R3*i2-V2:.4f} V\n")                   # Vo = -11.1963 V

# ======================================================
# Opción 2: Supuesto D1: RUPTURA y D2: ON
# ======================================================

# Matriz de coeficientes
A = np.array([[R1 + R2, -R2],[-R2, R2 + R3]])

# Vector de términos independientes
b = np.array([-V1 - Vz, Vz + Vj + V2])

# Resolver el sistema
x = np.linalg.solve(A, b)

i1, i2 = x

print(f"Supuesto D1: RUPTURA y D2: ON")
print(f"i1 = {i1:.6f} A e i2 = {i2:.6f} A")           # i1 = -0.033003 A e i2 = -0.001856 A
print(f"Id1 = {i2-i1:.6f} A e Id2 = {-i2:.6f} A\n")   # Id1 = 0.031147 A e Id2 = 0.001856 A

# ======================================================
# Opción 3: Supuesto D1: RUPTURA y D2: OFF
# ======================================================

i1 = - (V1 + Vz) / (R1 + R2)

i2 = 0

print(f"Supuesto D1: RUPTURA y D2: OFF")
print(f"i1 = {i1:.6f} A e i2 = 0 A")    # i1 = -0.031739 A e i2 = 0 A
print(f"Id1 = {-i1:.6f} A\n")             # Id1 = 0.031739 A

# ======================================================
# Opción 4: Supuesto D1: OFF y D2: ON
# ======================================================

i = (Vj + V2 - V1) / (R1 + R3)

print(f"Supuesto D1: OFF y D2: ON")
print(f"i = {i:.6f} A")                             # i = -0.010641 A
print(f"Vd1 = {V1 + R1*i:.6f} e Id2 = {-i:.6f} A")  # Vd1 = 15.658974 e Id2 = 0.010641 A