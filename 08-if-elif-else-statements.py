# Sentencias if

username = 'Tony'
password = '123456'

# if condicion:
#   bloque_de_codigo
# elif condicion:
#   bloque_de_codigo
# elif condicion:
#   bloque_de_codigo
# else:
#   bloque_de_codigo_alternativo

if username == 'Tony' and password == '123456':
    print('Acceso permitido')
else:
    print('Acceso denegado')

# Ejemplo con la logica del juego de Super Mario

personaje = 'Mario'
salta = True
obstaculo = True
cantidad_vidas = 3

if obstaculo and salta:
    print(f'{personaje} salta y evita el obstaculo')
# elif obstaculo == False:
elif not obstaculo:  # como aprendimos se puede poner not para negar la condicion y es lo mismo que obstaculo == False
    print(f'No pasa nada, {personaje} sigue su curso')
else:
    print(f'{personaje} no salta y no evita el obstaculo')
    print(f'{personaje} pierde una vida')
    cantidad_vidas -= 1
    print(f'Le quedan {cantidad_vidas} vidas')
