"""
Ejemplo 6: Escriba una función que le permita calcular el factorial de un número.

Autor: Rodrigo Martínez Campos
Fecha: Agosto 2025
"""
import math

def factorial_iterativo(n):
    if n==0 or n==1:
        return 1
    else:
        resultado = 1
        for i in range(2, n+1):
            resultado = resultado * i
        return resultado


def factorial_recursivo(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursivo(n-1)

print(math.factorial(6))

print(factorial_iterativo(6))

print(factorial_recursivo(6))