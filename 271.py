def empieza_con_minuscula(cadena):
    # Verificar si la cadena empieza con una letra minúscula
    if len(cadena) > 0 and cadena[0].islower():
        return True
    else:
        return False

# Ejemplos de uso
cadena1 = "python"
cadena2 = "Python"
cadena3 = ""

resultado1 = empieza_con_minuscula(cadena1)
resultado2 = empieza_con_minuscula(cadena2)
resultado3 = empieza_con_minuscula(cadena3)

print(f'¿{cadena1} empieza con minúscula? {resultado1}')
print(f'¿{cadena2} empieza con minúscula? {resultado2}')
print(f'¿La cadena vacía empieza con minúscula? {resultado3}')
