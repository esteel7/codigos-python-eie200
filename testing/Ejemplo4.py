""" 
Ejemplo 4: Escriba una función que calcule 1/x y arroje un mensaje de error al dividir por cero.

Autor: Rodrigo Martínez Campos
Fecha: Agosto 2025
"""
def getReciprocal(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero.")

print(getReciprocal(5)) # Salida: 0.2
print(getReciprocal(0)) # Salida: Error: No es posible dividir por cero.