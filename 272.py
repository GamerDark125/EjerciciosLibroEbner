def es_repeticion(cadena):
    longitud = len(cadena)

    # Verificar si la cadena tiene una longitud par y está formada por la repetición de una subcadena
    for i in range(1, longitud // 2 + 1):
        subcadena = cadena[:i]
        repeticiones = longitud // i
        if subcadena * repeticiones == cadena:
            return True

    return False

# Ejemplos de uso
cadena1 = "abab"
cadena2 = "ababab"
cadena3 = "abcabcabc"
cadena4 = "abcd"

resultado1 = es_repeticion(cadena1)
resultado2 = es_repeticion(cadena2)
resultado3 = es_repeticion(cadena3)
resultado4 = es_repeticion(cadena4)

print(f'¿{cadena1} es una repetición? {resultado1}')
print(f'¿{cadena2} es una repetición? {resultado2}')
print(f'¿{cadena3} es una repetición? {resultado3}')
print(f'¿{cadena4} es una repetición? {resultado4}')
