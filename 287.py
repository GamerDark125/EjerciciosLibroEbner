def cadena_mas_larga(lista_cadenas):
    # Si la lista está vacía, devolvemos None
    if not lista_cadenas:
        return None

    # Inicializamos la cadena más larga con la primera cadena de la lista
    cadena_mas_larga = lista_cadenas[0]

    # Iteramos sobre el resto de cadenas en la lista
    for cadena in lista_cadenas[1:]:
        # Comparamos la longitud de la cadena actual con la longitud de la cadena más larga
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena

    return cadena_mas_larga

# Ejemplo de uso
lista_ejemplo = ['Pepe', 'Juan', 'María', 'Ana']
resultado = cadena_mas_larga(lista_ejemplo)
print(f'La cadena más larga en la lista es: {resultado}')
