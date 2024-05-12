# 1 Dadas las variables a = 450 y b = 60, imprime en pantalla si a es igual a b, si es mayor o menor que b

a = 450
b = 60

# Tu solución

if a == b:
    print(f'{a} es igual a {b}')
elif a > b:
    print(f'{a} es mayor que {b}')
else:
    print(f'{a} es menor que {b}')


# 2 Dada la variable x = 45, imprime en pantalla si es divisible entre 3 y 5

# Pista: puedes usar el operador de residuo (%), si un numero es divisible entre un numero dado
# su residuo es 0

x = 45

# Tu solución
if x % 3 == 0 and x % 5 == 0:
    print(f'{x} es divisible entre 3 y 5')
else:
    print(f'{x} no es divisible entre 3 y 5')

# 3 Dale el valor que desees a la variable password e imprime en pantalla
# si es muy corta "❌ Contraseña muy corta"
# si es muy larga "❌ Contraseña muy larga"
# siendo muy corta si tiene menos de 6 caracteres y muy larga si tiene mas de 12 caracteres
# si cumple estas dos condiciones imprime "✅ Contraseña aceptable"

# Pista: puedes usar la función de longitud len() para obtener la longitud de una cadena

password = 'BCUBCncue8783493nBEU'

print(len(password))

# Tu solución

if len(password) < 6:
    print('❌ Contraseña muy corta')
elif len(password) > 12:
    print('❌ Contraseña muy larga')
else:
    print('✅ Contraseña aceptable')
