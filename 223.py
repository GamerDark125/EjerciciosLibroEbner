# Asignar una lista a la variable a
a = [1, 2, 3, 4, 5]

# Crear una lista (b) mediante el slicing de la lista a
b = a[1:3]

# Asignar la lista a la variable c
c = a

# Crear una copia de la lista a (d)
d = a[:]

# Comparar listas
result1 = a == c
result2 = a == d
result3 = c == d
result4 = a == b

# Comparar identidades
result5 = a is c
result6 = a is d
result7 = c is d
result8 = a is b

# Mostrar resultados
print(result1)  # Devolverá True
print(result2)  # Devolverá True
print(result3)  # Devolverá True
print(result4)  # Devolverá False
print(result5)  # Devolverá True
print(result6)  # Devolverá False
print(result7)  # Devolverá True
print(result8)  # Devolverá False
