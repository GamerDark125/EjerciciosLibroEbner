import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def juego_de_la_vida_toroidal(tablero):
    filas, columnas = tablero.shape
    nuevo_tablero = np.zeros_like(tablero)

    for y in range(filas):
        for x in range(columnas):
            vecinos = contar_vecinos_toroidales(tablero, y, x)
            if tablero[y, x] == 0 and vecinos == 3:
                nuevo_tablero[y, x] = 1
            elif tablero[y, x] == 1 and (vecinos == 2 or vecinos == 3):
                nuevo_tablero[y, x] = 1

    return nuevo_tablero

def contar_vecinos_toroidales(tablero, y, x):
    filas, columnas = tablero.shape
    n = (
        tablero[(y - 1) % filas, (x - 1) % columnas] +
        tablero[(y - 1) % filas, x] +
        tablero[(y - 1) % filas, (x + 1) % columnas] +
        tablero[y, (x - 1) % columnas] +
        tablero[y, (x + 1) % columnas] +
        tablero[(y + 1) % filas, (x - 1) % columnas] +
        tablero[(y + 1) % filas, x] +
        tablero[(y + 1) % filas, (x + 1) % columnas]
    )
    return n

def generar_tablero_inicial_toroidal(filas, columnas, densidad):
    return np.random.choice([0, 1], size=(filas, columnas), p=[1 - densidad, densidad])

def actualizar_toroidal(frameNum, img, tablero):
    nuevo_tablero = juego_de_la_vida_toroidal(tablero)
    img.set_array(nuevo_tablero)
    tablero[:,:] = nuevo_tablero
    return img,

# Configurar parámetros
filas = 50
columnas = 50
densidad = 0.2

# Generar el tablero inicial
tablero_toroidal = generar_tablero_inicial_toroidal(filas, columnas, densidad)

# Configurar la animación
fig, ax = plt.subplots()
img = ax.imshow(tablero_toroidal, cmap='binary', interpolation='nearest')
ani = animation.FuncAnimation(fig, actualizar_toroidal, fargs=(img, tablero_toroidal),
                              frames=100, interval=200, save_count=50, repeat=False)
plt.show()
