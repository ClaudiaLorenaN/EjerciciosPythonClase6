#ejercicio6

def login(usuario, password):
  if usuario == 'usuario1' and password == '1234':
    print('Usuario y contraseña validos, puede ingresar')
  else:
    print('Usuario y contraseña NO validos')


usuario = input('Por favor ingresar un nombre de usuario')
password = input('Por favor ingresar una contraseña')

login(usuario, password)