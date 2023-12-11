def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4 y no divisible por 100, excepto si es divisible por 400.
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_anio(anio):
    # Si el año es bisiesto, devuelve 366; de lo contrario, devuelve 365.
    return 366 if es_bisiesto(anio) else 365

# Solicitar al usuario que ingrese el año
anio = int(input("Ingrese un año: "))

# Obtener el número de días en el año ingresado
numero_dias = dias_en_anio(anio)

# Mostrar el resultado
print(f'El año {anio} tiene {numero_dias} días.')
