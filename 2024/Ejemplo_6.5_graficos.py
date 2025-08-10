import numpy as np
import matplotlib.pyplot as plt

# Gráfico 1
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(1)
plt.plot(x,y)
plt.title("Gráfica de la función sen(x)")
#plt.grid('both')
plt.xlabel('x')
plt.ylabel('sen(x)')
plt.show()

# Gráfico 2
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x, y, 'bo')
ax[0,1].plot(x, z, 'rx')
ax[1,0].plot(x, y)
ax[1,0].plot(x, z)
ax[1,0].legend(['sin', 'cos'])
ax[1,1].plot(x, y+z, linewidth = 4)
ax[1,1].legend(['sin(x) + cos(s)'])
plt.show()