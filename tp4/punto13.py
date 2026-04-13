segundos_totales = int(input("Ingresá una cantidad de segundos: "))

horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

print(f"Tiempo: {horas:02}:{minutos:02}:{segundos:02}")
