def menu():
    opcion = ''
    while len(opcion) != 1 or opcion not in 'abc':
        print('Cajero automático.')
        print('a) Ingresar dinero.')
        print('b) Sacar dinero.')
        print('c) Consultar saldo.')
        opcion = input('Escoja una opción: ')
        if len(opcion) != 1 or opcion not in 'abc':
            print('Sólo puede escoger las letras a, b o c. Inténtelo de nuevo.')
    return opcion

# Ejemplo de uso
eleccion = menu()
print(f'Ha elegido la opción: {eleccion}')
