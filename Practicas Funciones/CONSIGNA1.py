#consigna1 
errores = 0

año = int(input("Ingrese el año: "))

while año != 0:

    mes = int(input("Ingrese mes: "))

    while mes < 1 or mes > 12:
        print("Mes incorrecto. Reingrese:")
        errores += 1
        mes = int(input("Ingrese mes: "))

    auto = int(input("Ingrese la cantidad de autos: "))

    año = int(input("Ingrese el año: "))

print(f"Cantidad de errores del operador: {errores}")
