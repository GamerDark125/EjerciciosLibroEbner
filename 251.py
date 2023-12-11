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

# Función para multiplicar una matriz por un número
def multiplicar_matriz(matriz, numero):
    resultado = [[elemento * numero for elemento in fila] for fila in matriz]
    return resultado

# Solicitar al usuario las dimensiones de la matriz
filas = int(input("Introduce el número de filas: "))
columnas = int(input("Introduce el número de columnas: "))

# Leer la matriz
print("Introduce la matriz:")
matriz = leer_matriz(filas, columnas)

# Solicitar al usuario el número
numero = int(input("Introduce el número para multiplicar la matriz: "))

# Multiplicar la matriz por el número
if matriz is not None:
    resultado = multiplicar_matriz(matriz, numero)
    print("Matriz resultante:")
    imprimir_matriz(resultado)
