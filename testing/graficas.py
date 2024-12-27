import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de t y x
t = np.linspace(-2, 2, 400)
x = np.linspace(-2, 2, 400)

# Función escalar f(x) = x^2
f_x = x**2

# Función vectorial F(t) = (t, t^2)
F1_t = t
F2_t = t**2

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico de la función escalar f(x) = x^2
ax[0].plot(x, f_x, label=r"$f(x) = x^2$")
ax[0].set_title("Función Escalar $f(x) = x^2$")
ax[0].set_xlabel("x")
ax[0].set_ylabel("f(x)")
ax[0].grid(True)
ax[0].legend()

# Gráfico de la función vectorial F(t) = (t, t^2)
ax[1].plot(F1_t, F2_t, label=r"$\mathbf{F}(t) = (t, t^2)$")
ax[1].quiver(F1_t[::40], F2_t[::40], np.ones_like(F1_t[::40]), 2*F1_t[::40], scale=20, color='r')
ax[1].set_title("Función Vectorial $\mathbf{F}(t) = (t, t^2)$")
ax[1].set_xlabel("x(t)")
ax[1].set_ylabel("y(t)")
ax[1].grid(True)
ax[1].legend()

plt.tight_layout()
plt.show()
