def maxima_diferencia_absoluta_entre_pares_con_cero(lista):
    # Si la lista tiene menos de dos elementos, o si contiene un cero, devolvemos 0
    if len(lista) < 2 or 0 in lista:
        return 0

    # Encontrar el valor máximo y mínimo de la lista
    maximo_valor = max(lista)
    minimo_valor = min(lista)

    # Calcular la máxima diferencia entre cualquier par de elementos
    max_diferencia = abs(maximo_valor - minimo_valor)

    return max_diferencia

# Ejemplo de uso
lista_ejemplo = [1, 10, 2, 6, 8, 20]
resultado = maxima_diferencia_absoluta_entre_pares_con_cero(lista_ejemplo)
print(f'El valor absoluto de la máxima diferencia entre cualquier par de elementos (con cero) es: {resultado}')
