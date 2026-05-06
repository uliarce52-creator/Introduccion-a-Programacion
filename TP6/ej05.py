# TP VI - Ejercicio 5
# Ingresar 10 números e informar si cada uno es positivo, negativo o cero

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    if numero > 0:
        print(f"{numero} es positivo.")
    elif numero < 0:
        print(f"{numero} es negativo.")
    else:
        print(f"{numero} es cero.")
