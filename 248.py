# Definir el tamaño de la matriz
filas = 4
columnas = 4

# Crear una matriz identidad de 4x4
matriz_identidad = [[1 if i == j else 0 for j in range(columnas)] for i in range(filas)]

# Mostrar la matriz identidad
for fila in matriz_identidad:
    print(fila)
