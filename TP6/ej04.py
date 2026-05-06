# TP VI - Ejercicio 4
# Calcular el factorial de un número ingresado por el usuario

n = int(input("Ingrese un número entero: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial de {n} es: {factorial}")
