elemento = 5
lista = [1, 4, 5, 1, 3, 8]

pertenece = False  # Inicializar la variable fuera del bucle

for i in lista:
    if elemento == i:
        pertenece = True
        break  # Salir del bucle cuando se encuentra el elemento

if pertenece:
    print('Pertenece')
else:
    print('No pertenece')

#Cambios realizados:
#
#Se inicializa pertenece fuera del bucle para que no se reinicie en cada iteración.
#Se agrega break después de establecer pertenece en True para salir del bucle tan pronto como se encuentra el elemento.
#En el código original, cada iteración del bucle establece pertenece en True o False, pero el resultado final solo reflejará el estado de pertenece después de la última comparación. Con la corrección, el programa funcionará correctamente y mostrará si el elemento pertenece o no a la lista.
