# TP VII - Ejercicio 3
# Leer un número entero entre 1 y 100 con validación

numero_valido = False

while not numero_valido:
    entrada = input("Ingrese un número entero entre 1 y 100: ")
    
    if not entrada.lstrip('-').isdigit():
        print("El dato ingresado no es numérico.")
    else:
        numero = int(entrada)
        if numero < 1 or numero > 100:
            print("El número ingresado está fuera del rango permitido.")
        else:
            numero_valido = True

print(f"{numero} es válido. ¡Gracias!")
