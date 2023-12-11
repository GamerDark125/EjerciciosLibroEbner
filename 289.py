def prefijo_comun_mas_largo(lista_cadenas):
    # Si la lista está vacía, no hay prefijo común
    if not lista_cadenas:
        return ""
    # Ordenamos la lista para facilitar la comparación
    lista_cadenas.sort()

    # Tomamos la primera y última cadena (las más pequeña y grande)
    primer_cadena = lista_cadenas[0]
    ultima_cadena = lista_cadenas[-1]
    # Iteramos sobre las letras de la primera cadena
    for i in range(len(primer_cadena)):
        # Si la letra actual no coincide entre la primera y la última cadena, encontramos el prefijo
        if primer_cadena[i] != ultima_cadena[i]:
            return primer_cadena[:i]

    # Si llegamos aquí, todas las letras son iguales hasta la longitud de la cadena más corta
    return primer_cadena
# Ejemplo de uso
lista_ejemplo = ['poliedro', 'policía', 'polífona', 'polinizar', 'polaridad', 'política']
resultado = prefijo_comun_mas_largo(lista_ejemplo)
print(f'El prefijo común más largo en la lista es: {resultado}')
