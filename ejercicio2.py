#ejercicio2

def calcularTemperaturaPromedio(temperaturamaxima, temperaturaminima):
  resultado = (temperaturamaxima + temperaturaminima)/2
  return resultado


temperaturamaxima = int(input("Por favor ingresar temperatura máxima"))
temperaturaminima = int(input("Por favor ingresar temperatura mínima"))

resultado = calcularTemperaturaPromedio(temperaturamaxima, temperaturaminima)
print(f'La temperatura promedio es {resultado}')