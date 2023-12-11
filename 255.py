# Matriz de ejemplo 5x5
matriz_ejemplo = [
    [1, -2, 3, 4, -5],
    [6, 7, -8, 9, 10],
    [-11, 12, 13, -14, 15],
    [16, -17, 18, 19, 20],
    [21, 22, -23, 24, 25]
]

# Función para determinar si una matriz es prima
def es_matriz_prima(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Calcular la suma de elementos de cada fila y columna
    sumas_filas = [sum(fila) for fila in matriz]
    sumas_columnas = [sum(matriz[i][j] for i in range(filas)) for j in range(columnas)]
    
    # Verificar si alguna fila tiene la misma suma que alguna columna
    return any(suma_fila in sumas_columnas for suma_fila in sumas_filas)

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

# Determinar si la matriz es prima y mostrar el resultado
if es_matriz_prima(matriz_ejemplo):
    print("\nLa matriz es prima.")
else:
    print("\nLa matriz no es prima.")
