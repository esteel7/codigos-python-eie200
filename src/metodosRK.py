import numpy as np

def Euler(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros_like(x)
    y[0] = y0

    # Desarrollar el método de Euler
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[i])
        y[i+1] = y[i] + k1 * h
    
    return x, y

def Heun(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros_like(x)
    y[0] = y0

    # Desarrollar el método de Heun
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[i]) #pendiente en (xi, yi)
        k2 = dydx(x[i]+ h, y[i] + k1*h) # Pendiente en (xi+h, yi+1)
        y[i+1] = y[i] + 0.5*(k1 + k2) * h # Estimamos y[i+1] con el promedio de las pendientes k1 y k2
    
    return x, y

def PuntoMedio(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros_like(x)
    y[0] = y0

    # Desarrollar el método del Punto Medio
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[i]) #pendiente en (xi, yi)
        k2 = dydx(x[i]+ 0.5*h, y[i] + 0.5*k1*h) # Pendiente en (xi+0.5*h, yi+1/2)
        y[i+1] = y[i] + k2*h # Estimamos y[i+1] con la pendiente k2
    
    return x, y

def Ralston(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros_like(x)
    y[0] = y0

    # Desarrollar el método de Ralston
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[i]) #pendiente en (xi, yi)
        k2 = dydx(x[i]+ 0.75*h, y[i] + 0.75*k1*h) # Pendiente en (xi+0.75*h, yi+3/4)
        y[i+1] = y[i] + ((1/3)*k1 + (2/3)*k2)*h # Estimamos y[i+1]
    
    return x, y

def RK3(x_range, dydx, h, y0):
    
    # Definimos el arreglo x
    x_min = x_range[0]
    x_max = x_range[1]
    x = np.arange(x_min, x_max + h, h)

    # Definimos el arreglo y
    y = np.zeros_like(x)
    y[0] = y0

    # Desarrollar el método de Ralston
    for i in range(x.shape[0]- 1):
        k1 = dydx(x[i], y[i]) #pendiente en (xi, yi)
        k2 = dydx(x[i]+ 0.5*h, y[i] + 0.5*k1*h)
        k3 = dydx(x[i] + h, y[i] - k1*h + 2*k2*h)
        
        y[i+1] = y[i] + (1/6)*(k1 + 4*k2 + k3)*h # Estimamos y[i+1]
    
    return x, y