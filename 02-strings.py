
nombre = "Tony"

apellido = "Stark"

edad = 25

cita_textual = 'Tony dijo: "Estoy aprendiendo Python"'

cita_textual_ingles = 'Tony said: "I\'m learning Python"'

# print(cita_textual_ingles)

 # print(len(nombre))

# print(nombre[0:7])

# print(dir(nombre))

# print(nombre.title())

# print(nombre.count('a'))

# Concatenacion
# print(nombre, apellido)
# print('=' * 50 )
# print(apellido)

# Tony Stark tiene 25 años

print(f'{nombre} {apellido} tiene {edad} años') # la manera mas sencilla de concatenar datos
print(nombre, apellido, 'tiene', edad, 'años' ) # demasiadas comas
print(nombre + ' ' + apellido + ' tiene ' + str(edad) + ' años') # es necesario convertir todo a string
