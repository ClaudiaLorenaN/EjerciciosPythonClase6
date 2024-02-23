#ejercicio1

numero1 = int(input("Por favor ingresar el primer número: "))
numero2 = int(input("Por favor ingresar el segundo número: "))

if numero1 % numero2 == 0:
  print(f'{numero1} es multiplo del {numero2}')
else:
  print(f'{numero1} no es multiplo del {numero2}')
