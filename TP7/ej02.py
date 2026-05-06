# TP VII - Ejercicio 2
# Ingresar notas hasta que se ingrese -1, luego mostrar el promedio

total = 0
cantidad = 0

nota = float(input("Ingrese una nota (o -1 para terminar): "))

while nota != -1:
    total += nota
    cantidad += 1
    nota = float(input("Ingrese una nota (o -1 para terminar): "))

if cantidad > 0:
    promedio = total / cantidad
    print(f"La nota promedio es: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
