import numpy as np
import matplotlib.pyplot as plt

m = 2.5
g = 9.81
c = 1
v0 = 0

t = np.linspace(0, 10, 100)
velocidades = np.zeros_like(t)

v = v0

for i in range(1,t.size):  
    velocidades[i-1] = v
    v = v + (g - c*v/m)*(t[i]-t[i-1])

velocidades[t.size-1] = v

print(f"El valor final de caída es {v}")

plt.plot(t,velocidades)
plt.grid(True)
plt.show()