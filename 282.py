def calcular_productorio(lista):
    # Si la lista está vacía, el productorio es 1
    if not lista:
        return 1

    # Calcular el productorio
    productorio = 1
    for numero in lista:
        productorio *= numero

    return productorio

# Ejemplo de uso
lista_ejemplo = [1, 2, 3, 4, 5]
resultado = calcular_productorio(lista_ejemplo)
print(f'El productorio de la lista es: {resultado}')
