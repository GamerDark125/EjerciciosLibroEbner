def calcular_media(lista):
    # Si la lista está vacía, la media es cero
    if not lista:
        return 0

    # Calcular la media
    suma = sum(lista)
    media = suma / len(lista)

    return media

# Ejemplo de uso
lista_ejemplo = [1, 2, 3, 4, 5]
resultado = calcular_media(lista_ejemplo)
print(f'La media de la lista es: {resultado}')
