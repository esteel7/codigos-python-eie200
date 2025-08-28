""" 
Ejemplo 4: Escriba una función que calcule 1/x y arroje un mensaje de error al dividir por cero.

Autor: Rodrigo Martínez Campos
Fecha: Agosto 2025
"""
def obtenerReciproco(x):
    try: 
        return 1/x
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero.")
    except TypeError:
        print("Error: Debe ingresar un número (int o float)")

x = float(input("Ingrese un número: "))
print(f"Se ingresa el valor {x} y su recíproco es {obtenerReciproco(x)}")
