import numpy as np
import matplotlib.pyplot as plt

def caida_libre(t, m, c, v0 = 0, g = 9.81):
    '''
    Esta función calcula la velocidad de caída de un cuerpo de masa m.

    Parameters
    -----------
    t: numpy.ndarray
        Vector de tiempo 
    m: float
        Masa del cuerpo
    c: float
        Coeficiente de arrastre
    v0: float, optional
        Velocidad inicial
    g: float, optional
        Aceleración de gravedad

    Returns
    --------
    float
        Velocidad final de caída
    ''' 

    v = v0 *np.exp(-c*t/m) + (g*m/ c)*(1 - np.exp(-c*t/m))

    plt.plot(t, v)
    plt.grid(True)

    plt.show()

    return v[-1]


t = np.linspace(0, 10, 100)

print(f"La velocidad de caída final es: {caida_libre(t, 2.5, 1, 5)} m/s")

