#ejercicio 5

import math
def calcularPerimetroCircunferencia(pi, radio):
  return(pi*(radio**2))

pi = math.pi
radio = 5
resultado = calcularPerimetroCircunferencia(pi, radio)
print(resultado)