def maximo(lista):
    # Inicializamos max_actual con el primer elemento de la lista
    max_actual = lista[0]

    # Iteramos sobre el resto de elementos de la lista
    for elemento in lista[1:]:
        # Comparamos el elemento actual con max_actual
        if elemento > max_actual:
            # Si el elemento es mayor, actualizamos max_actual
            max_actual = elemento

    # Devolvemos el valor máximo encontrado
    return max_actual

# Llamada a la función
resultado = maximo([6, 2, 7, 1, 10, 1, 0])

# Mostramos el resultado
print(f'El valor máximo en la lista es: {resultado}')
