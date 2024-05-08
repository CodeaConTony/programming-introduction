# Ejercicios con datos numéricos

# Puedes crear variables si es necesario

#1 Calcular el perímetro de un rectángulo e imprimir el resultado
# Fórmula:  2 * (base + altura)

# Tu solución
base = 8
altura = 4
perimetro_rectangulo = 2 * (base + altura)
print(perimetro_rectangulo)

#2 Convertir 25 grados Celcius a Fahrenheit
# Fórmula: (celsius * 9/5) + 32

# Tu solución
temperatura_actual_celsius = 25
temperatura_fahrenheit = (temperatura_actual_celsius * 9/5) + 32
print(temperatura_fahrenheit)

#3 Redondear 9.86998 con 3 decimales

# Tu solución
print(round(9.86998, 3))

#4 Calcular el valor absoluto de -155

# Tu solución
print(abs(-155))

#5 Calcular la raíz cuadrada de 841
# Averigua como importar sqrt y como usarlo

# Tu solución
from math import sqrt

print(sqrt(841))

#6 Convertir '0xff0a' a int

# Tu solución
print(int('0xff0a', 16))

#7 Convertir 8674 a binario

# Tu solución
print(bin(8674))
