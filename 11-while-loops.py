# while loop

# while condicion:
#   bloque_de_codigo

# while True:
#   if condicion:
#     break


username = input('Ingresa un nombre de usuario: ')

password = input('Ingresa una contraseña: ')

while True:
    if len(password) < 6:
        print('❌ Contraseña muy corta. Ingresa una contraseña entre 6 y 12 caracteres')
        password = input('Ingresa una contraseña: ')
    elif len(password) > 12:
        print('❌ Contraseña muy larga. Ingresa una contraseña entre 6 y 12 caracteres')
        password = input('Ingresa una contraseña: ')
    else:
        print('✅ Contraseña aceptable')
        break

contador = 0

while True:
    print(f'Numero {contador}')
    contador += 1
    if contador <= 10:
        continue
    break
