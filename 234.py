def eliminar_elementos_pares(lista):
    resultado = [elemento for elemento in lista if elemento % 2 != 0]
    return resultado

# Ejemplo de uso
lista_original = [1, -2, 1, -5, 0, 3]
lista_resultante = eliminar_elementos_pares(lista_original)

print("Lista original:", lista_original)
print("Lista resultante eliminando elementos de valor par:", lista_resultante)
