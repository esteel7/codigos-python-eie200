import numpy as np
import matplotlib.pyplot as plt

# Definir la malla de puntos en el plano xy
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Definir las componentes del campo vectorial F(x, y) = (2xy, -x)
U = 2 * X * Y  # Componente en x
V = -X         # Componente en y

# Definir la trayectoria r(t) = (3t^2, -1) para t en [0, 1]
t = np.linspace(0, 1, 100)
x_traj = 3 * t**2
y_traj = -1 * np.ones_like(t)  # y = -1 para toda t

# Crear la gráfica
plt.figure(figsize=(8, 8))

# Graficar el campo vectorial
plt.quiver(X, Y, U, V, color='blue', alpha=0.5)

# Graficar la trayectoria r(t) con dirección
plt.plot(x_traj, y_traj, 'r', label=r'$\mathbf{r}(t) = (3t^2, -1)$')
plt.arrow(x_traj[-2], y_traj[-2], 
          x_traj[-1] - x_traj[-2], y_traj[-1] - y_traj[-2],
          head_width=0.15, head_length=0.15, fc='red', ec='red')

# Configurar límites, etiquetas, y leyenda
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Campo Vectorial $\mathbf{F}(x, y) = (2xy, -x)$ y Trayectoria $\mathbf{r}(t) = (3t^2, -1)$')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()