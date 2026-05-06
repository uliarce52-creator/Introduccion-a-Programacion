# TP VI - Ejercicio 8
# Precipitaciones diarias de una semana: promedio y día de mayor lluvia

dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

total = 0
max_lluvia = -1
dia_max = ""

for i in range(7):
    lluvia = float(input(f"Ingrese los ml de lluvia del {dias[i]}: "))
    total += lluvia
    if lluvia > max_lluvia:
        max_lluvia = lluvia
        dia_max = dias[i]

promedio = total / 7

print(f"El promedio de precipitaciones fue de {promedio:.2f} ml diarios.")
print(f"El día de más precipitaciones fue el {dia_max}.")
