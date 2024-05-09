# Booleans
True
False

es_administrador = False
print(es_administrador)

# Operadores de igualdad
print(4 > 5) # False
print(4 < 6) # True
print(4 <= 5) # True
print(4 >= 6) # False
print(4 == 4) # True
print(4 != 5) # True

# Operadores logicos
print(not 4 == 5)  # True
print(4 > 3 and 4 < 2) # True - False -> False
print(4 > 3 or 4 < 2) # True - False -> True

# # Operadores de asignación
a = 4
b = 5

a += 4
# a = a + 4
print(a) # 8

b -= 1
# b = b - 1
print(b) # 4

a **= 2
a = a ** 2
print(a) # 64

a *= 2 # 128
# a = a *2
a /= 4 # 32
# a = a / 4
print(a) # 32
