# Solicitar un entero positivo n
n = int(input("Introduce un entero positivo n: "))

# Validar que n sea positivo
while n <= 0:
    print("Por favor, introduce un entero positivo.")
    n = int(input("Introduce un entero positivo n: "))

# Crear la matriz identidad de n x n
matriz_identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Mostrar la matriz identidad
for fila in matriz_identidad:
    print(fila)
