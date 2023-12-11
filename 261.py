import matplotlib.pyplot as plt

def aplicar_reglas_especificas(estado):
    nuevas_celdas = []
    reglas = {'000': 0, '001': 1, '010': 1, '011': 0, '100': 1, '101': 1, '110': 0, '111': 1}
    
    for i in range(len(estado)):
        vecindad = ''.join([str(estado[(i + j) % len(estado)]) for j in range(-1, 2)])
        nuevas_celdas.append(reglas[vecindad])

    return nuevas_celdas

def automata_celular_grafico(pulsos):
    longitud_universo = 41  # Longitud del universo, debe ser impar para tener una celda central
    estado_actual = [0] * longitud_universo
    estado_actual[len(estado_actual) // 2] = 1  # Inicializa con una célula viva en el centro

    fig, ax = plt.subplots()

    for _ in range(pulsos):
        ax.imshow([estado_actual], cmap='binary', interpolation='nearest')
        estado_actual = aplicar_reglas_especificas(estado_actual)
    
    plt.title('Evolución del Autómata Celular Unidimensional')
    plt.xlabel('Celdas')
    plt.ylabel('Pulsos')
    plt.show()

# Solicitar el número de pulsos al usuario
pulsos = int(input("Ingrese el número de pulsos: "))

# Ejecutar el autómata celular con las reglas específicas y representación gráfica
automata_celular_grafico(pulsos)
