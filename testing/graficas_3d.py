import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Crear una figura 3D
fig = plt.figure(figsize=(15, 10))

# Ejemplo 1: Superficie 3D de una función z = x^2 + y^2
ax1 = fig.add_subplot(131, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title("Superficie 3D: $z = x^2 + y^2$")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# Ejemplo 2: Curva paramétrica en 3D
ax2 = fig.add_subplot(132, projection='3d')
t = np.linspace(0, 10, 400)
x2 = np.sin(t)
y2 = np.cos(t)
z2 = t
ax2.plot(x2, y2, z2, label='Curva helicoidal')
ax2.set_title("Curva Helicoidal en 3D")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
ax2.legend()

# Ejemplo 3: Campo vectorial en 3D
ax3 = fig.add_subplot(133, projection='3d')
x3, y3, z3 = np.meshgrid(np.linspace(-2, 2, 5),
                         np.linspace(-2, 2, 5),
                         np.linspace(-2, 2, 5))
u = -y3
v = x3
w = np.ones_like(z3)
ax3.quiver(x3, y3, z3, u, v, w, length=0.2, color='blue')
ax3.set_title("Campo Vectorial 3D")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Z")

plt.tight_layout()
plt.show()
