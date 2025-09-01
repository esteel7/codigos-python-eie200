import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure(1)
#plt.figure(2, figsize=(8, 4), dpi=100, facecolor='lightgray')
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()