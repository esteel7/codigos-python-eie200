import numpy
import matplotlib.pyplot as plt

# Definimos la frecuencia de la sinusoide
omega = np.pi*np.array([1, 2, 3])

# Definimos la variable temporal
t = np.linspace(0, 10, 200)

# Iteramos sobre cada frecuencia y graficamos la sinusoide
fig, ax = plt.subplots(1,3)
for i in range(len(omega):
ax[i].plot(t, np.sin(omega[i]*t))
  ax[i].legend(['omega={:f}'.format(omega[i])])
plt.show()