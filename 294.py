def producto_q(a, b):
    if a > b or (a <= 0 and 0 <= b):
        # Si a es mayor que b o 0 está entre a y b, devolver 0
        return 0
    else:
        # Calcular el producto de los números desde a hasta b
        resultado = 1
        for i in range(a, b + 1):
            resultado *= i
        return resultado

# Solicitar al usuario los valores de a y b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Calcular y mostrar Qb^{i=a} i
resultado_producto_q = producto_q(a, b)
print(f'El producto Qb^{i=a} i es: {resultado_producto_q}')
