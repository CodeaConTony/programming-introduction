# 1 Escribe un loop while que imprima lo que el usuario ingrese
# Hasta que el usuario ingrese 'STOP'.

# Tu solución

import random
entrada_usuario = input("Escriba algo: ")

while entrada_usuario != 'STOP':
    print(entrada_usuario)
    entrada_usuario = input("Escriba algo o 'STOP' para detener: ")


# 2 Escribe un loop que le pida al usuario que adivine un numero secreto
# El numero secreto debe estar entre 1 y 100 y debe ser un numero aleatorio

# Pista: Use el modulo 'random' para obtener un numero aleatorio entre 1 y 100
# Averigua como hacerlo
# Imprima mensaje de error si el usuario pone un numero mayor o menor que el secreto
# Imprima un mensaje de felicitaciones cuando el usuario adivine el numero

# Tu solución

numero_secreto = random.randint(1, 100)

print('Adivina un número entre 1-100')
print('=' * 15)
while True:
    entrada_usuario = int(input("Adivine el numero: "))
    if entrada_usuario == numero_secreto:
        print(f"Felicitaciones, adivinaste el numero secreto: {numero_secreto}")
        break
    elif entrada_usuario > numero_secreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")

# 3 Escribe un loop que imprima la tabla de multiplicar de un numero dado por el usuario
# Debe detenerse cuando el multiplicador sea 10

# Pista: guarde el valor del multiplicador en una variable y aumente su valor en 1

# Tu solución
multiplicador = 1

numero = int(input("Ingresa un numero: "))

while multiplicador <= 10:
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
    multiplicador += 1
