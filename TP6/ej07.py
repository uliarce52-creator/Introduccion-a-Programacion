# TP VI - Ejercicio 7
# Ingresar 10 números y mostrar el máximo, el mínimo y sus posiciones

max_numero = None
min_numero = None
pos_max = 0
pos_min = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    if max_numero is None or numero > max_numero:
        max_numero = numero
        pos_max = i
    if min_numero is None or numero < min_numero:
        min_numero = numero
        pos_min = i

print(f"El mayor número ingresado es {max_numero}, y lo ingresaste en la posición {pos_max}.")
print(f"El menor número ingresado es {min_numero}, y lo ingresaste en la posición {pos_min}.")
