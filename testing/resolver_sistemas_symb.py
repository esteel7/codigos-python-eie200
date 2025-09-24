import sympy as sp

# ======================================================
# Sección 1: Ejemplo con números reales
# ======================================================

# Definir variables

R1, R2, R3, V1, V2, Vj, i1, i2 = sp.symbols('R1 R2 R3 V1 V2 Vj i1 i2')

# Ecuaciones
eq1 = sp.Eq((R1+R2)*i1 - R2*i2, Vj -V1)
eq2 = sp.Eq(-R2*i1 + (R2+R3)*i2, -V2)

# Resolver simbólicamente
sol = sp.solve((eq1, eq2), (i1, i2))
print(sol)

# ======================================================
# Sección 2: Ejemplo considerando números complejos
# ======================================================

# Variables
i1, i2 = sp.symbols('i1 i2')

# Impedancias simbólicas
Z1 = 10 + 5*sp.I
Z2 = 4 - 2*sp.I
Z3 = 8*sp.I
V1 = 12 + 3*sp.I
V2 = -6*sp.I
Vj = 1

# Ecuaciones
eq1 = sp.Eq((Z1+Z2)*i1 - Z2*i2, Vj - V1)
eq2 = sp.Eq(-Z2*i1 + (Z2+Z3)*i2, -V2)

# Resolver simbólicamente
sol = sp.solve((eq1, eq2), (i1, i2))
print(sol)