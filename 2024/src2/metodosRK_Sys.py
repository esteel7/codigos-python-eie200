import numpy as np

def Euler(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros([len(y0), len(x)])
    
    # Aplicamos la condición inicial
    y[:, 0] = y0[:]

    # Desarrollar el método de Euler
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[:,i])
        y[:,i+1] = y[:,i] + k1 * h
    
    return x, y

def RK4(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros([len(y0), len(x)])
    y[:,0] = y0[:]

    # Desarrollar el método RK4
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[:,i]) #pendiente en (xi, yi)
        k2 = dydx(x[i]+ 0.5*h, y[:,i] + 0.5*k1*h)
        k3 = dydx(x[i] + 0.5*h, y[:,i] + 0.5*k2*h)
        k4 = dydx(x[i] + h, y[:,i] + k3*h)
        
        y[:,i+1] = y[:,i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h # Estimamos y[i+1]
    
    return x, y