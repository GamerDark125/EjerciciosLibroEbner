def maxima_diferencia_absoluta(lista):
    # Si la lista tiene menos de dos elementos, no hay diferencia que calcular
    if len(lista) < 2:
        return None

    # Inicializar la máxima diferencia con la diferencia entre el primer y segundo elemento
    max_diferencia = abs(lista[1] - lista[0])

    # Iterar sobre los elementos consecutivos y actualizar la máxima diferencia si es necesario
    for i in range(1, len(lista) - 1):
        diferencia_actual = abs(lista[i + 1] - lista[i])
        max_diferencia = max(max_diferencia, diferencia_actual)

    return max_diferencia

# Ejemplo de uso
lista_ejemplo = [1, 10, 2, 6, 2, 0]
resultado = maxima_diferencia_absoluta(lista_ejemplo)
print(f'El valor absoluto de la máxima diferencia consecutiva es: {resultado}')
