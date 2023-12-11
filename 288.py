def cadenas_mas_largas(lista_cadenas):
    # Si la lista está vacía, devolvemos una lista vacía
    if not lista_cadenas:
        return []

    # Encontramos la longitud máxima de las cadenas en la lista
    longitud_maxima = max(len(cadena) for cadena in lista_cadenas)

    # Filtramos las cadenas que tienen la longitud máxima
    cadenas_mas_largas = [cadena for cadena in lista_cadenas if len(cadena) == longitud_maxima]

    return cadenas_mas_largas

# Ejemplo de uso
lista_ejemplo = ['Pepe', 'Ana', 'Juan', 'Paz']
resultado = cadenas_mas_largas(lista_ejemplo)
print(f'Las cadenas más largas en la lista son: {resultado}')
