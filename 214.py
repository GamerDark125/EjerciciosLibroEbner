# Evaluando la expresión [1][0]
resultado1 = [1][0]
print(resultado1)  # Salida: 1

# Evaluando la expresión [][0]
# Esto generará un IndexError, ya que estamos intentando acceder al primer elemento de una lista vacía.
try:
    resultado2 = [][0]
except IndexError as e:
    print(f"Error: {e}")
