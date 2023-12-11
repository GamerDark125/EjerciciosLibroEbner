def posicion_inicio_serie_mas_larga(lista):
    # Inicializamos variables para la serie más larga
    inicio_serie_actual = 0
    longitud_serie_actual = 1

    # Inicializamos variables para la serie más larga encontrada hasta el momento
    inicio_serie_mas_larga = 0
    longitud_serie_mas_larga = 1

    # Si la lista es vacía, no hay series
    if not lista:
        return None

    # Iteramos sobre el resto de elementos de la lista
    for i in range(1, len(lista)):
        # Si el elemento es igual al anterior, pertenece a la misma serie
        if lista[i] == lista[i - 1]:
            longitud_serie_actual += 1
        else:
            # Si la serie actual es más larga que la serie más larga encontrada hasta el momento,
            # actualizamos las variables de la serie más larga
            if longitud_serie_actual > longitud_serie_mas_larga:
                inicio_serie_mas_larga = inicio_serie_actual
                longitud_serie_mas_larga = longitud_serie_actual

            # Comenzamos una nueva serie
            inicio_serie_actual = i
            longitud_serie_actual = 1

    # Aseguramos que la última serie también se compare
    if longitud_serie_actual > longitud_serie_mas_larga:
        inicio_serie_mas_larga = inicio_serie_actual

    return inicio_serie_mas_larga

# Ejemplo de uso
lista_ejemplo = [1, 1, 8, 8, 8, 8, 0, 0, 0, 2, 10, 10]
resultado = posicion_inicio_serie_mas_larga(lista_ejemplo)
print(f'La serie más larga empieza en la posición {resultado}.')
