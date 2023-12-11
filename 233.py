def eliminar_elementos_indices_pares(lista):
    resultado = [lista[i] for i in range(len(lista)) if i % 2 != 0]
    return resultado

# Ejemplo de uso
lista_original = [1, 2, 1, 5, 0, 3]
lista_resultante = eliminar_elementos_indices_pares(lista_original)

print("Lista original:", lista_original)
print("Lista resultante eliminando elementos de índice par:", lista_resultante)
