def obtener_lista_palabras(cadena):
    palabras = set()  # Utilizamos un conjunto para evitar duplicados
    for palabra in cadena.split():
        palabra_min = palabra.lower()
        palabras.add(palabra_min)
    return list(palabras)

# Ejemplo de uso
cadena = 'Una frase formada con palabras. Otra frase con otras palabras.'
lista_palabras = obtener_lista_palabras(cadena)

print("Lista de palabras en minúsculas sin duplicados:")
print(lista_palabras)
