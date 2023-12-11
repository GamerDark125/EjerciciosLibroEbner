def contar_series(lista):
    # Inicializamos el contador de series
    num_series = 0

    # Si la lista es vacía, no hay series
    if not lista:
        return num_series

    # Inicializamos la serie con el primer elemento de la lista
    serie_actual = [lista[0]]

    # Iteramos sobre el resto de elementos de la lista
    for elemento in lista[1:]:
        # Si el elemento es igual al último de la serie actual, pertenece a la misma serie
        if elemento == serie_actual[-1]:
            serie_actual.append(elemento)
        else:
            # Si el elemento es diferente, incrementamos el contador de series y comenzamos una nueva serie
            num_series += 1
            serie_actual = [elemento]

    # Aseguramos que la última serie también se cuente
    num_series += 1

    return num_series

# Ejemplo de uso
lista_ejemplo = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10]
resultado = contar_series(lista_ejemplo)
print(f'La lista tiene {resultado} series.')
