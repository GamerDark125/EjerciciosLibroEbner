def son_amigos(num1, num2):
    def suma_divisores(n):
        return sum(i for i in range(1, n) if n % i == 0)

    return suma_divisores(num1) == num2 and suma_divisores(num2) == num1

# Solicitar al usuario los números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar si los números son amigos y mostrar el resultado
resultado = son_amigos(numero1, numero2)
print(f'¿Los números {numero1} y {numero2} son amigos? {resultado}')
