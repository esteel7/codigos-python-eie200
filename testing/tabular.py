from tabulate import tabulate

# Ejemplo de uso de la librería tabulate para imprimir tablas en Python
# Datos de ejemplo
# Lista de listas con nombres de ríos y sus longitudes

rios1 = [['Almanzora', 105],
         ['Guadiaro', 79],
         ['Guadalhorce', 154],
         ['Guadalmedina', 51.5]]

# Imprime tabla a partir de los datos de los ríos        
print(tabulate(rios1))