"""
Ejemplo 5: Escriba una función de Python que reciba la edad de una persona como un argumento
y que indique si esa persona es menor de edad, mayor de edad o adulto mayor. Considere que una
persona mayor a 60 años se considera un adulto mayor.

Autor: Rodrigo Martínez Campos
Fecha: Agosto 2025
"""
def obtenerRangoEtario(edad):
    if edad < 18:
        return "Menor de edad"
    elif edad > 60:
        return "Adulto mayor"
    else:
        return "Mayor de edad"

for i in (5, 17, 18, 34, 62):
    print(f"Si tiene {i} años, es {obtenerRangoEtario(i)}")