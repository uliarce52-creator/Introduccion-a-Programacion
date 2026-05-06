# TP VI - Ejercicio 6
# Ingresar 10 números y mostrar el máximo y su posición

max_numero = None
pos_max = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    if max_numero is None or numero > max_numero:
        max_numero = numero
        pos_max = i

print(f"El mayor número ingresado es {max_numero}, y lo ingresaste en la posición {pos_max}.")
