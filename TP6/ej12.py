# TP VI - Ejercicio 12
# Calcular el factorial de un número n

n = int(input("Ingrese un número entero positivo: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")
