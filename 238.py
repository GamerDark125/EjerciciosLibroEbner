letra = input('Dame una letra: ')
if len(letra) == 1 and ('a' <= letra <= 'z' or letra in 'áéíóúüñ'):
    print(letra, 'es una letra minúscula')
