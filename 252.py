# Matriz de ejemplo 3x4
matriz_ejemplo = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Función para imprimir una matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para calcular la traspuesta de una matriz
def traspuesta_matriz(matriz):
    traspuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return traspuesta

# Mostrar la matriz original
print("Matriz original:")
imprimir_matriz(matriz_ejemplo)

# Calcular y mostrar la traspuesta de la matriz
traspuesta = traspuesta_matriz(matriz_ejemplo)
print("\nTraspuesta de la matriz:")
imprimir_matriz(traspuesta)
