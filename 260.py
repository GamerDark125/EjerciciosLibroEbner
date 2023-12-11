def aplicar_reglas_especificas(estado):
    nuevas_celdas = []
    reglas = {'000': 0, '001': 1, '010': 1, '011': 0, '100': 1, '101': 1, '110': 0, '111': 1}
    
    for i in range(len(estado)):
        vecindad = ''.join([str(estado[(i + j) % len(estado)]) for j in range(-1, 2)])
        nuevas_celdas.append(reglas[vecindad])

    return nuevas_celdas

def automata_celular_personalizado(pulsos):
    longitud_universo = 41  # Longitud del universo, debe ser impar para tener una celda central
    estado_actual = [0] * longitud_universo
    estado_actual[len(estado_actual) // 2] = 1  # Inicializa con una célula viva en el centro

    for _ in range(pulsos):
        print(''.join(['*' if celda == 1 else ' ' for celda in estado_actual]))
        estado_actual = aplicar_reglas_especificas(estado_actual)

# Solicitar el número de pulsos al usuario
pulsos = int(input("Ingrese el número de pulsos: "))

# Ejecutar el autómata celular con las reglas específicas
automata_celular_personalizado(pulsos)
    