def solucion_ecuacion_lineal(a, b):
    if a == 0:
        # Si a es cero, la ecuación no es lineal
        if b == 0:
            # Si b también es cero, hay infinitas soluciones
            return "Infinitas soluciones"
        else:
            # Si b no es cero, no hay solución
            return None
    else:
        # Calcular la solución para x
        x = -b / a
        return x

# Solicitar al usuario los valores de a y b
coeficiente_a = float(input("Ingrese el valor de a: "))
coeficiente_b = float(input("Ingrese el valor de b: "))

# Calcular y mostrar la solución de la ecuación lineal
solucion = solucion_ecuacion_lineal(coeficiente_a, coeficiente_b)
print(f'La solución de la ecuación es: {solucion}')
