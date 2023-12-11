# Matriz de ejemplo 5x5
matriz_ejemplo = [
    [1, 2, 3, 4, 5],
    [0, 6, 7, 8, 9],
    [0, 0, 10, 11, 12],
    [0, 0, 0, 13, 14],
    [0, 0, 0, 0, 15]
]

# Función para determinar si una matriz es diagonal superior
def es_diagonal_superior(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(i + 1, columnas):
            # Verificar si hay elementos no nulos por debajo de la diagonal principal
            if matriz[i][j] != 0:
                return False
    return True

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

# Determinar si la matriz es diagonal superior y mostrar el resultado
if es_diagonal_superior(matriz_ejemplo):
    print("\nLa matriz es diagonal superior.")
else:
    print("\nLa matriz no es diagonal superior.")
