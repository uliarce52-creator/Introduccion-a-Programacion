# TP VI - Ejercicio 10
# Registro de cepillado de dientes durante una semana

dias_3_o_mas = 0
dias_sin_cepillar = 0
max_cepilladas = 0
total = 0

for i in range(1, 8):
    veces = int(input(f"¿Cuántas veces se cepilló el día {i}? "))
    total += veces
    if veces >= 3:
        dias_3_o_mas += 1
    if veces == 0:
        dias_sin_cepillar += 1
    if veces > max_cepilladas:
        max_cepilladas = veces

promedio = total / 7

if max_cepilladas <= 1:
    print("Higiene insuficiente")

if dias_sin_cepillar > 0:
    print(f"Días sin cepillarse: {dias_sin_cepillar}")

print(f"Días con 3 o más cepilladas: {dias_3_o_mas}")
print(f"Promedio de cepilladas diarias: {promedio:.2f}")
