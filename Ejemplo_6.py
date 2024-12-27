def factorial(n):
    '''
    Esta función calcula el factorial de un número iterativamente.

    El argumento es:
        n: entero (numero para el cual se calcula el factorial)
    '''
    if type(n) == int:

        resultado = 1

        for i in range(1, n+1):
            resultado = resultado * i

        return resultado
    else:
        print("No se puede calcular el número no entero.")

#for num in range(11):
#    print(f"El factorial de {num} es {factorial(num)}")

factorial(3.4)
