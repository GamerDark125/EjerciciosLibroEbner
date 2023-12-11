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

# Función para imprimir un vector
def imprimir_vector(vector):
    print(vector)

# Función para calcular el vector v
def calcular_vector_v(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Inicializar el vector v con ceros
    vector_v = [0] * columnas
    
    # Calcular la suma de cada columna
    for j in range(columnas):
        suma_columna = sum(matriz[i][j] for i in range(filas))
        vector_v[j] = suma_columna
    
    return vector_v

# Solicitar al usuario las dimensiones de la matriz
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

# Leer la matriz
print("Introduce la matriz:")
matriz = leer_matriz(filas, columnas)

# Calcular y mostrar el vector v
if matriz is not None:
    vector_v = calcular_vector_v(matriz)
    print("Vector v:")
    imprimir_vector(vector_v)
