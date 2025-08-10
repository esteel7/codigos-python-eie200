def factorial_recursivo(n):
    '''
    Esta función calcula el factorial de un número recursivamente.

    El argumento es:
        n: entero (numero para el cual se calcula el factorial)
    '''
    if type(n) == int:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial_recursivo(n-1)
    else:
        print("No se puede calcular el factorial de un número no entero.")

for num in range(11):
    print(f"El factorial de {num} es {factorial_recursivo(num)}")