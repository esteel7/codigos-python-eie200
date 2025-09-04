import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def aproximar_seno(x: np.ndarray, n_max: int):
    """
    Aproxima sin(x) mediante su serie de Maclaurin hasta n_max términos
    y grafica todas las aproximaciones acumuladas en una misma ventana.

    Parámetros
    ----------
    x : np.ndarray
        Vector de puntos del dominio donde evaluar.
    n_max : int
        Número de términos de la serie (iteraciones del acumulado).

    Retorna
    -------
    fig : matplotlib.figure.Figure
        Figura con todos los gráficos en un mismo eje.
    """
    # Referencia
    y_ref = np.sin(x)

    # Inicializar serie acumulada
    serie = np.zeros_like(x, dtype=float)

    # Crear UNA sola figura y un solo eje
    fig, ax = plt.subplots(figsize=(8, 5))

    # Graficar referencia
    ax.plot(x, y_ref, 'x', label="Referencia: sin(x)")

    # Lista de leyendas para las aproximaciones
    legends = []

    # Aproximaciones acumuladas
    for n in range(n_max):
        legends.append(f"n = {n}")
        serie += (-1)**n * x**(2*n + 1) / factorial(2*n + 1)
        ax.plot(x, serie, alpha=0.9)  # cada curva en el mismo eje

    # Ajustes del gráfico
    ax.set_xlim(float(np.min(x)), float(np.max(x)))
    ax.set_ylim(-1.1, 1.1)
    ax.grid(True)
    ax.set_title("Aproximación de sin(x) con serie de Maclaurin")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(["Referencia: sin(x)"] + legends, loc="best")

    # No mostramos aquí; devolvemos la figura
    return fig

x = np.linspace(0, 2*np.pi, 400)
fig = aproximar_seno(x, n_max=10)
plt.show()