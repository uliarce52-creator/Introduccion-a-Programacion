# TP VI - Ejercicio 9
# Cuadras caminadas con el perro durante N días

dias = int(input("¿Cuántos días desea registrar? "))

total_cuadras = 0
max_cuadras = -1
dia_max = 0
hubo_mas_de_30 = False

for i in range(1, dias + 1):
    cuadras = int(input(f"Ingrese las cuadras caminadas el día {i}: "))
    total_cuadras += cuadras
    if cuadras > max_cuadras:
        max_cuadras = cuadras
        dia_max = i
    if cuadras > 30:
        hubo_mas_de_30 = True

promedio = total_cuadras / dias

print(f"\nTotal de cuadras caminadas: {total_cuadras}")
print(f"Promedio de cuadras por día: {promedio:.2f}")
print(f"Día en que más caminó: día {dia_max}")

if hubo_mas_de_30:
    print("El perro necesita 24 horas de descanso")
elif promedio < 10 and max_cuadras <= 20:
    print("El perro necesita caminar más")
