import numpy as np

def resolver_edo_rk3(f_edo, i0, t0, tf, h, params=None):
    """
    Resuelve una EDO escalar de la forma:
        di/dt = f_edo(t, i, params)
    usando el método de Runge–Kutta de 3er orden (RK3).

    Parámetros
    ----------
    f_edo : función
        Función que representa la EDO, con firma:
            f_edo(t, i, params) -> di/dt
    i0 : float
        Corriente inicial i(t0).
    t0 : float
        Tiempo inicial.
    tf : float
        Tiempo final.
    h : float
        Paso de integración.
    params : dict, opcional
        Diccionario con los parámetros del problema (por ejemplo,
        V0, omega, R, L0, alpha en el circuito RL).

    Retorna
    -------
    t : np.ndarray
        Arreglo con los tiempos usados.
    i : np.ndarray
        Arreglo con las corrientes calculadas i(t) en cada tiempo t.
    """
    if params is None:
        params = {}

    # Número de pasos (se asume que (tf - t0) / h es entero)
    N = int((tf - t0) / h)

    # Arreglos para tiempo y corriente
    t = np.zeros(N + 1)
    i = np.zeros(N + 1)

    # Condiciones iniciales
    t[0] = t0
    i[0] = i0

    # Bucle de integración con RK3
    for n in range(N):
        t_n = t[n]
        i_n = i[n]

        k1 = f_edo(t_n,           i_n,                 params)
        k2 = f_edo(t_n + 0.5*h,   i_n + 0.5*h*k1,      params)
        k3 = f_edo(t_n + h,       i_n - h*k1 + 2*h*k2, params)

        i[n+1] = i_n + (h/6.0) * (k1 + 4*k2 + k3)
        t[n+1] = t_n + h

    # La función devuelve las corrientes calculadas (y los tiempos)
    return t, i
