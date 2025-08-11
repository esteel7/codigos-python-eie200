'''
Este es un encabezado de código donde se pueden ver las 

'''

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)

# Así podemos imprimir el último elemento del array
print(a[-1])

# Al igual que la lista que usamos para crear el array, el mismo array también es mutable
a[0] = 10
print(a)

# También se puede usar notación para cortar o acortar los arrays
a[:3] # array([10,2, 3])

# One major difference is that slice indexing of a list copies the elements into a new list, 
# but slicing an array returns a view: an object that refers to the data in the original array. 
# The original array can be mutated using the view.

b = a[3:]

b[0] = 40

print(a) #El elemento 3 de a se ve modificado

a = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])

print(a)
print(a[1, 3])

# How to create a basic array https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-create-a-basic-array

# crea un arreglo de ceros (float64 por defecto)
c = np.zeros(3)

d = np.zeros(3, dtype=np.int64)

# And even an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number, and the step size.

e = np.arange(2, 9, 2)

# Podemos crear un arrya con valores que estén espaciados linealmente

f = np.linspace(0, 10, 10)

print(f)

# Pruebas con arreglos

x = np.array([[3, 4, 5], [2, 3, -1]])

print(f"{x} de tipo {type(x)}")
print(f"{x.shape} de tipo {type(x.shape)}")

y0 = np.array([3, 5, 6])

a = np.zeros_like(y0)

a[:] = y0[:]

print(a)

b = np.zeros([4, 5])

print(b)