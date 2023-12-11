# Corregido para Python 3
letra = input('Dame una letra: ')
if (len(letra) == 1 and 'a' <= letra <= 'z') or letra in ['á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']:
    print(letra, 'es una letra minúscula')
