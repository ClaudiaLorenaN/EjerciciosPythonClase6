#ejercicio7

def login():
  cantidadDeIntentos = 1
  while cantidadDeIntentos <= 3:
    usuario = input('Por favor ingresar un nombre de usuario')
    password = input('Por favor ingresar una contraseña')
    if usuario == 'usuario1' and password == '1234':
      print('Usuario y contraseña validos, puede ingresar')
      break
    else:
      print('Usuario y contraseña NO validos')
      cantidadDeIntentos = cantidadDeIntentos + 1
        

login()