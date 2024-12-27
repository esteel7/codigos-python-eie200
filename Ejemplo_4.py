def division(x):
  a = None
  try:
    a = 1/x
  except:
    print('No se puede dividir por 0')
  return a

def division_v2(x):
  if x == 0:    
    print('No se puede dividir por 0')
    a = None
  else:
    a = 1/x
  return a

#print(division(0))
#print(division_v2(0))

numero = float(input("Ingrese un número: "))

print(division(numero))

# rodrigo.martinez@pucv.cl

# Inscripción Grupo EIE200-1