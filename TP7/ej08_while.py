# TP VII - Ejercicio 8
# Todos los ejercicios del TP VI rehechos con while en lugar de for
# Cada ejercicio está separado como una función para mayor claridad

# ------------------------------------------------------------
# Ejercicio 1: Primeros 100 números enteros positivos
# ------------------------------------------------------------
def ej1():
    n = 1
    while n <= 100:
        print(n)
        n += 1

# ------------------------------------------------------------
# Ejercicio 2: Solo los números pares del 1 al 100
# ------------------------------------------------------------
def ej2():
    n = 1
    while n <= 100:
        if n % 2 == 0:
            print(n)
        n += 1

# ------------------------------------------------------------
# Ejercicio 3: Suma de los números del 75 al 150
# ------------------------------------------------------------
def ej3():
    suma = 0
    n = 75
    while n <= 150:
        suma += n
        n += 1
    print(f"La suma de los números del 75 al 150 es: {suma}")

# ------------------------------------------------------------
# Ejercicio 4: Factorial de un número
# ------------------------------------------------------------
def ej4():
    n = int(input("Ingrese un número entero: "))
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"El factorial de {n} es: {factorial}")

# ------------------------------------------------------------
# Ejercicio 5: 10 números e informar si son positivos, negativos o cero
# ------------------------------------------------------------
def ej5():
    i = 1
    while i <= 10:
        numero = int(input(f"Ingrese el número {i}: "))
        if numero > 0:
            print(f"{numero} es positivo.")
        elif numero < 0:
            print(f"{numero} es negativo.")
        else:
            print(f"{numero} es cero.")
        i += 1

# ------------------------------------------------------------
# Ejercicio 6: 10 números, mostrar el máximo y su posición
# ------------------------------------------------------------
def ej6():
    max_numero = None
    pos_max = 0
    i = 1
    while i <= 10:
        numero = int(input(f"Ingrese el número {i}: "))
        if max_numero is None or numero > max_numero:
            max_numero = numero
            pos_max = i
        i += 1
    print(f"El mayor número ingresado es {max_numero}, y lo ingresaste en la posición {pos_max}.")

# ------------------------------------------------------------
# Ejercicio 7: 10 números, mostrar máximo y mínimo con sus posiciones
# ------------------------------------------------------------
def ej7():
    max_numero = None
    min_numero = None
    pos_max = 0
    pos_min = 0
    i = 1
    while i <= 10:
        numero = int(input(f"Ingrese el número {i}: "))
        if max_numero is None or numero > max_numero:
            max_numero = numero
            pos_max = i
        if min_numero is None or numero < min_numero:
            min_numero = numero
            pos_min = i
        i += 1
    print(f"El mayor número ingresado es {max_numero}, y lo ingresaste en la posición {pos_max}.")
    print(f"El menor número ingresado es {min_numero}, y lo ingresaste en la posición {pos_min}.")

# ------------------------------------------------------------
# Ejercicio 8: Precipitaciones de la semana
# ------------------------------------------------------------
def ej8():
    dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    total = 0
    max_lluvia = -1
    dia_max = ""
    i = 0
    while i < 7:
        lluvia = float(input(f"Ingrese los ml de lluvia del {dias[i]}: "))
        total += lluvia
        if lluvia > max_lluvia:
            max_lluvia = lluvia
            dia_max = dias[i]
        i += 1
    promedio = total / 7
    print(f"El promedio de precipitaciones fue de {promedio:.2f} ml diarios.")
    print(f"El día de más precipitaciones fue el {dia_max}.")

# ------------------------------------------------------------
# Ejercicio 9: Cuadras caminadas con el perro
# ------------------------------------------------------------
def ej9():
    dias = int(input("¿Cuántos días desea registrar? "))
    total_cuadras = 0
    max_cuadras = -1
    dia_max = 0
    hubo_mas_de_30 = False
    i = 1
    while i <= dias:
        cuadras = int(input(f"Ingrese las cuadras caminadas el día {i}: "))
        total_cuadras += cuadras
        if cuadras > max_cuadras:
            max_cuadras = cuadras
            dia_max = i
        if cuadras > 30:
            hubo_mas_de_30 = True
        i += 1
    promedio = total_cuadras / dias
    print(f"\nTotal de cuadras caminadas: {total_cuadras}")
    print(f"Promedio de cuadras por día: {promedio:.2f}")
    print(f"Día en que más caminó: día {dia_max}")
    if hubo_mas_de_30:
        print("El perro necesita 24 horas de descanso")
    elif promedio < 10 and max_cuadras <= 20:
        print("El perro necesita caminar más")

# ------------------------------------------------------------
# Ejercicio 10: Cepillado de dientes
# ------------------------------------------------------------
def ej10():
    dias_3_o_mas = 0
    dias_sin_cepillar = 0
    max_cepilladas = 0
    total = 0
    i = 1
    while i <= 7:
        veces = int(input(f"¿Cuántas veces se cepilló el día {i}? "))
        total += veces
        if veces >= 3:
            dias_3_o_mas += 1
        if veces == 0:
            dias_sin_cepillar += 1
        if veces > max_cepilladas:
            max_cepilladas = veces
        i += 1
    promedio = total / 7
    if max_cepilladas <= 1:
        print("Higiene insuficiente")
    if dias_sin_cepillar > 0:
        print(f"Días sin cepillarse: {dias_sin_cepillar}")
    print(f"Días con 3 o más cepilladas: {dias_3_o_mas}")
    print(f"Promedio de cepilladas diarias: {promedio:.2f}")

# ------------------------------------------------------------
# Ejercicio 11: Horas de juego
# ------------------------------------------------------------
def ej11():
    total_horas = 0
    dias_mas_5 = 0
    dias_cero = 0
    primer_dia_cero = None
    i = 1
    while i <= 10:
        horas = int(input(f"¿Cuántas horas jugó el día {i}? "))
        total_horas += horas
        if horas == 0 and primer_dia_cero is None:
            primer_dia_cero = i
        if horas == 0:
            dias_cero += 1
        if horas > 5:
            dias_mas_5 += 1
        i += 1
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

# ------------------------------------------------------------
# Ejercicio 12: Factorial con while
# ------------------------------------------------------------
def ej12():
    n = int(input("Ingrese un número entero positivo: "))
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"{n}! = {factorial}")


# --- Menú para ejecutar cada ejercicio ---
print("TP VII - Ejercicio 8: TP VI con while")
print("Seleccione qué ejercicio ejecutar (1-12): ")
opcion = int(input())

if opcion == 1: ej1()
elif opcion == 2: ej2()
elif opcion == 3: ej3()
elif opcion == 4: ej4()
elif opcion == 5: ej5()
elif opcion == 6: ej6()
elif opcion == 7: ej7()
elif opcion == 8: ej8()
elif opcion == 9: ej9()
elif opcion == 10: ej10()
elif opcion == 11: ej11()
elif opcion == 12: ej12()
else: print("Opción inválida.")
