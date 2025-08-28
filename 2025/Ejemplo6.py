"""
Ejemplo 6: Escriba una función que le permita calcular el factorial de un número.

# f(n) = 1*2*3*...*n

Autor: Rodrigo Martínez Campos
Fecha: Agosto 2025
"""
import math

def factorial_iterativo(n):
    if n==0 or n==1:
        return 1
    elif type(n) == int and n > 1:
        resultado = 1
        for i in range(2,n+1):
            resultado = resultado * i
        return resultado
    else:
        print("Error: Debe ingresar un número entero >=0")

def factorial_recursivo(n):
    if n==0:
        return 1
    elif type(n) == int and n > 0:
        return n*factorial_recursivo(n-1)
    else:
        print("Error: Debe ingresar un número entero >=0")
        
print(factorial_iterativo(6))
print(factorial_recursivo(6))
print(math.factorial(6))

