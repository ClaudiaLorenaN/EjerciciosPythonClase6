#ejercicio3

def calcularTemperaturaPromedio(temperaturamaxima, temperaturaminima):
  resultado = (temperaturamaxima + temperaturaminima)/2
  return resultado

cantidadDeDias = int(input("Por favor ingresar la cantidad de días "))
dia = 1

while dia <= cantidadDeDias:
  temperaturamaxima = int(input(f' Por favor ingresar temperatura máxima para el día {dia} '))
  temperaturaminima = int(input(f' Por favor ingresar temperatura mínima para el día {dia} ' ))
  resultado = calcularTemperaturaPromedio(temperaturamaxima, temperaturaminima)
  print(f'La temperatura promedio del día {dia}  es {resultado} ')
  dia = dia + 1