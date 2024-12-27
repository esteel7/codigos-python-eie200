import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2* np.pi, 100)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(2,2)
ax[0, 0].plot(x, y, 'bo')
ax[0, 1].plot(x, z, 'rx')
ax[1, 0].plot(x, y)
ax[1, 0].plot(x, z)

ax[0, 0].set_title("sin(x)")
ax[0, 1].set_title("cos(x)")
ax[1, 0].set_title("sin(x) y cos(x)")
ax[1, 1].set_title("sin(x) + cos(x)")

ax[1, 0].legend(['sin', 'cos'])
ax[1, 1].plot(x, y + z, linewidth = 3)
ax[1, 1].legend(["sin(x) + cos(x)"])

plt.show()
