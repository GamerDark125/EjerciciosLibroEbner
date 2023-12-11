texto = "Este es un ejemplo. Aquí hay otra frase. Y una tercera."

# Dividir el texto en frases
frases = texto.split('.')

# Iterar sobre cada frase y contar el número de palabras
for i, frase in enumerate(frases, 1):
    # Filtrar las cadenas vacías que resultan del split
    palabras = [palabra for palabra in frase.split() if palabra]
    
    # Mostrar el número de palabras de cada frase
    print(f"Frase {i}: Número de palabras = {len(palabras)}")
