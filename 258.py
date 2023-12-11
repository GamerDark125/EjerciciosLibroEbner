import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def juego_de_la_vida_parametrizado(tablero, regla_nacimiento, regla_supervivencia, regla_aislamiento, regla_superpoblacion):
    filas, columnas = tablero.shape
    nuevo_tablero = np.zeros_like(tablero)

    for y in range(filas):
        for x in range(columnas):
            vecinos = contar_vecinos(tablero, y, x)
            if tablero[y, x] == 0 and vecinos == regla_nacimiento:
                nuevo_tablero[y, x] = 1
            elif tablero[y, x] == 1 and vecinos in regla_supervivencia:
                nuevo_tablero[y, x] = 1

    return nuevo_tablero

def contar_vecinos(tablero, y, x):
    filas, columnas = tablero.shape
    n = -tablero[y, x]

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= y + i < filas and 0 <= x + j < columnas:
                n += tablero[y + i, x + j]

    return n

def generar_tablero_inicial(filas, columnas, densidad):
    return np.random.choice([0, 1], size=(filas, columnas), p=[1 - densidad, densidad])

def actualizar(frameNum, img, tablero, regla_nacimiento, regla_supervivencia, regla_aislamiento, regla_superpoblacion):
    nuevo_tablero = juego_de_la_vida_parametrizado(tablero, regla_nacimiento, regla_supervivencia, regla_aislamiento, regla_superpoblacion)
    img.set_array(nuevo_tablero)
    tablero[:,:] = nuevo_tablero
    return img,

# Solicitar al usuario los parámetros
filas = int(input("Introduce el número de filas del tablero: "))
columnas = int(input("Introduce el número de columnas del tablero: "))
densidad = float(input("Introduce la densidad inicial de celdas vivas (valor entre 0 y 1): "))
regla_nacimiento = int(input("Introduce el número de vecinos para regla de nacimiento: "))
regla_supervivencia = [int(x) for x in input("Introduce los números de vecinos para regla de supervivencia (separados por espacios): ").split()]
regla_aislamiento = int(input("Introduce el número de vecinos para regla de aislamiento: "))
regla_superpoblacion = int(input("Introduce el número de vecinos para regla de superpoblación: "))

# Generar el tablero inicial
tablero = generar_tablero_inicial(filas, columnas, densidad)

# Configurar la animación
fig, ax = plt.subplots()
img = ax.imshow(tablero, cmap='binary', interpolation='nearest')
ani = animation.FuncAnimation(fig, actualizar, fargs=(img, tablero, regla_nacimiento, regla_supervivencia, regla_aislamiento, regla_superpoblacion),
                              frames=100, interval=200, save_count=50, repeat=False)
plt.show()
