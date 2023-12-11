#con la funcion sum
#def sumatorio_diferencia_contigua(lista):
#    # Utilizando la función sum y una comprensión de lista
#    return sum(lista[i + 1] - lista[i] for i in range(len(lista) - 1))
#
## Ejemplo de uso
#lista_ejemplo = [1, 3, 6, 10]
#resultado = sumatorio_diferencia_contigua(lista_ejemplo)
#print(f'El sumatorio de la diferencia entre números contiguos es: {resultado}')
            
#sin la funcion sum
def sumatorio_diferencia_contigua_sin_sum(lista):
    # Utilizando una expresión generadora
    return sum((lista[i + 1] - lista[i]) for i in range(len(lista) - 1))

# Ejemplo de uso
lista_ejemplo = [1, 3, 6, 10]
resultado = sumatorio_diferencia_contigua_sin_sum(lista_ejemplo)
print(f'El sumatorio de la diferencia entre números contiguos es: {resultado}')
