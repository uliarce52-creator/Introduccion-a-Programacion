# TP VII - Ejercicio 6
# Adivinar un número secreto entre 1 y 10

NUMERO_SECRETO = 7

intentos = 0
por_encima = 0
por_debajo = 0
adivinado = False

while not adivinado:
    intento = int(input("Ingrese un número entre 1 y 10: "))
    intentos += 1
    
    if intento == NUMERO_SECRETO:
        adivinado = True
    elif intento > NUMERO_SECRETO:
        por_encima += 1
        print("Demasiado alto.")
    else:
        por_debajo += 1
        print("Demasiado bajo.")

print(f"\n¡Correcto! El número secreto era {NUMERO_SECRETO}.")
print(f"Total de intentos: {intentos}")
print(f"Intentos por encima: {por_encima}")
print(f"Intentos por debajo: {por_debajo}")
