def sustituir_negativos_por_cero(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0

# Ejemplo de uso
lista_original = [1, -2, 3, -4, 5, -6]
print("Lista original:", lista_original)

# Sustituir elementos negativos por cero
sustituir_negativos_por_cero(lista_original)

# Mostrar la lista resultante
print("Lista después de sustituir negativos por cero:", lista_original)
