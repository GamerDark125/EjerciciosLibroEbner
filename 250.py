# Función para leer una matriz desde el usuario
def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [int(x) for x in input().split()]
        if len(fila) != columnas:
            print("Error: El número de columnas no coincide.")
            return None
        matriz.append(fila)
    return matriz

# Función para imprimir una matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para calcular la diferencia entre dos matrices
def diferencia_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Error: Las matrices no tienen el mismo tamaño.")
        return None
    resultado = [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
    return resultado

# Solicitar al usuario las dimensiones de las matrices
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

# Leer las dos matrices
print("Introduce la primera matriz:")
matriz1 = leer_matriz(filas, columnas)

print("Introduce la segunda matriz:")
matriz2 = leer_matriz(filas, columnas)

# Calcular y mostrar la diferencia entre las matrices
if matriz1 is not None and matriz2 is not None:
    diferencia = diferencia_matrices(matriz1, matriz2)
    if diferencia is not None:
        print("Diferencia entre las matrices:")
        imprimir_matriz(diferencia)
