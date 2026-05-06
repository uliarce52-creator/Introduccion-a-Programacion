# TP VII - Ejercicio 4
# Ingresar nombres hasta "fin" y contar cuántas veces se repite el primero

nombres = []
nombre = input("Ingrese un nombre (o 'fin' para terminar): ")

while nombre != "fin":
    nombres.append(nombre)
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")

if len(nombres) > 0:
    primer_nombre = nombres[0]
    contador = 0
    for n in nombres:
        if n == primer_nombre:
            contador += 1
    print(f"El nombre '{primer_nombre}' se repite {contador} vez/veces.")
else:
    print("No se ingresó ningún nombre.")
