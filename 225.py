# Solicitar al usuario el valor de n
n = int(input("Introduce un entero n: "))

# Crear una lista con range(1, n)
original_lista = list(range(1, n))

# Modificar la lista para que cada componente sea igual al cuadrado del componente original
cuadrado_lista = [x ** 2 for x in original_lista]

# Mostrar la lista resultante por pantalla
print(cuadrado_lista)
