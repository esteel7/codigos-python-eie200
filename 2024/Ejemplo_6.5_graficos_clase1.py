import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(1)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel('sen(x)')
plt.title("Gráfica de la función sen(x)")
plt.grid()
plt.show()