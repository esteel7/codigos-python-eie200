#Importar las librerías que usaremos (numpy y matplotlib)
import numpy as np
import matplotlib.pyplot as plt

# Definir la función que representa la expresión de la derivada dy/dt = f(t,y)
def dydt(t,y):
    return 4*np.exp(0.8*t)-0.5*y 

# Podemos definir la función exacta, con el objetivo de comparar nuestros resultados
def y_exacta(t):
    return (4/1.3)*(np.exp(0.8*t)-np.exp(-0.5*t))+2*np.exp(-0.5*t)

# Definimos parámetros y condiciones iniciales
t_inicio = 0
t_final = 4
y0 = 2
h = 1
# Inicializamos los vectores de t e y. Ayuda: Usar numpy.arange() si h es un float
t = np.arange(t_inicio,t_final+h,h) # t = [0, 1.0, 2.0, 3.0, 4.0]
y = np.zeros_like(t)                # y = [0 0 0 0 0]
y[0] = y0                           # y = [2 0 0 0 0]

# Implementamos el método de Euler, por ejemplo, con un for
for i in range(len(t)-1): # itera con i = 0, 1, 2, 3
    y[i+1] = y[i]+dydt(t[i],y[i])*h

# Obtenemos la solución exacta
t_exact = np.linspace(t_inicio, t_final, 100)
y_ref = y_exacta(t_exact)

# Graficamos y comparamos los resultados obtenidos con la solución exacta
plt.plot(t, y,'bo-', label='Método de Euler')
plt.plot(t_exact, y_ref, 'r-', label='Solución Exacta')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Comparación: Método de Euler vs Solución Exacta')
plt.legend()
plt.grid(True)
plt.show()