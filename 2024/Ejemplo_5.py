def verificar_edad(edad):
    '''
    Función que recibe la edad de una persona e indica si es menor
    de edad, mayor de edad o adulto mayor (mayor a 60 años).

    El argumento es:

        edad: punto flotante (edad en años)

    Retorna None
    '''

    if edad < 18:
        print("La persona es menor de edad.\n")
    elif edad > 60:
        print("La persona es un adulto mayor.\n")
    else:
        print("La persona es mayor de edad.\n")