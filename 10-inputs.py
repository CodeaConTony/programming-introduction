nombre = input("¿Cómo te llamas? ")
print('==============')
print(f"Hola {nombre}!")

# print(type(nombre))

edad = int(input("¿Cuantos años tienes? "))
print('==============')
print(f"{nombre}, tienes {edad} años.")

# print(type(edad))

print(f'El proximo año tendrás {edad + 1} años.')

peso = float(input("¿Cual es tu peso? "))
print('==============')
print(f'{nombre}, redondeando tu peso pesas {round(peso)} kilos.')

# Registro de usuario

username = input('Ingresa un nombre de usuario: ')

password = input('Ingresa una contraseña: ')

if len(password) < 6:
    print('❌ Contraseña muy corta')
elif len(password) > 12:
    print('❌ Contraseña muy larga')
else:
    print('✅ Contraseña aceptable')
