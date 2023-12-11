# Comparación de listas
result1 = [1, 2] == [1, 2]
print(result1)  # Devolverá True

# Identidad de listas
result2 = [1, 2] is [1, 2]
print(result2)  # Devolverá False

# Crear listas a y b
a = [1, 2, 3]
b = [a[0], a[1], a[2]]

# Comparación de listas a y b
result3 = a == b
print(result3)  # Devolverá True

# Identidad de listas a y b
result4 = a is b
print(result4)  # Devolverá False

# Comparación de elementos individuales
result5 = a[0] == b[1]
print(result5)  # Devolverá True

# Identidad de listas creadas con listas internas
result6 = b is [b[0], b[1], b[2]]
print(result6)  # Devolverá False
