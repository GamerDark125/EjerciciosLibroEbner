def comparar_listas(lista1, lista2):
    # Compara elementos uno por uno
    for elem1, elem2 in zip(lista1, lista2):
        if elem1 < elem2:
            return f"La lista1 ({lista1}) es menor que la lista2 ({lista2})."
        elif elem1 > elem2:
            return f"La lista1 ({lista1}) es mayor que la lista2 ({lista2})."

    # Verifica la longitud de las listas
    if len(lista1) < len(lista2):
        return f"La lista1 ({lista1}) es menor que la lista2 ({lista2})."
    elif len(lista1) > len(lista2):
        return f"La lista1 ({lista1}) es mayor que la lista2 ({lista2})."
    
    # Si llegamos aquí, las listas son iguales
    return f"La lista1 ({lista1}) es igual a la lista2 ({lista2})."

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [1, 2, 4]

resultado = comparar_listas(lista1, lista2)
print(resultado)
