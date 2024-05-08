
saludo = '¡Hola mundo!'

cadena = 'Soy un estudiante de Python'

#1 Calcular el tamaño de la cadena '¡Hola mundo!' e imprimir el resultado

# Tu solucion
print(len(saludo))
print(f'El saludo "{saludo}" tiene {len(saludo)} caracteres.')

#2 Extrae 'Soy un estudiante' del string 'Soy un estudiante de Python'}

# Tu solucion
print(cadena[0:17])

#3 Convertir la cadena 'Soy un estudiante de Python' a mayúsculas

# Tu solucion
print(cadena.upper())
print(cadena)
print(f"La cadena '{cadena}' en mayúsculas es '{cadena.upper()}'")

#4 Convertir la cadena 'Soy un estudiante de Python' a minúsculas

# Tu solucion
print(cadena.lower())
print(f"La cadena '{cadena}' en minusculas es '{cadena.lower()}'")

#5 Eliminar espacios en blanco de la cadena '    Soy un estudiante de Python   '

# Tu solucion
print('    Soy un estudiante de Python   '.strip())


#6 Contar la cantidad de apariciones de 't' en la cadena 'Soy un estudiante de Python'

# Tu solucion
frase = "Soy un estudiante de Python"
contador_t = frase.count("t")

print(f"La letra 't' aparece {contador_t} veces en la frase '{frase}'.")

print(cadena.count('t'))


#7 Reemplazar 'Python' por 'Java' en la cadena 'Soy un estudiante de Python'

# Tu solucion
print(cadena.replace('Python', 'Java'))

#8 Crea variables con tu nombre, apellido y edad
# e imprime el string 'Hola mi nombre es <nombre> <apellido> y tengo <edad> años'

# Tu solucion

mi_nombre = 'Tony'
mi_apellido = 'Stark'
mi_edad = 25

print(f'Hola mi nombre es {mi_nombre} {mi_apellido} y tengo {mi_edad} años')
