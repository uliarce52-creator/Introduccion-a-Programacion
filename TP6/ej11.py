# TP VI - Ejercicio 11
# Registro de horas de juego durante 10 días

total_horas = 0
dias_mas_5 = 0
dias_cero = 0
primer_dia_cero = None

for i in range(1, 11):
    horas = int(input(f"¿Cuántas horas jugó el día {i}? "))
    total_horas += horas
    if horas == 0 and primer_dia_cero is None:
        primer_dia_cero = i
    if horas == 0:
        dias_cero += 1
    if horas > 5:
        dias_mas_5 += 1

promedio = total_horas / 10

if primer_dia_cero is not None:
    print(f"El primer día que jugó 0 horas fue el día {primer_dia_cero}.")

print(f"Días en que jugó más de 5 horas: {dias_mas_5}")

if promedio > 3:
    print("Demasiadas horas frente a la pantalla")

if promedio <= 3 or dias_cero > 1:
    print(False)
else:
    print(True)
    print("Su hijo no excede las horas de juego")
