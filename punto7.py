nota1 = float(input(f"Ingrese la nota de su Primer Parcial: "))
nota2 = float(input(f"Ingrese la nota de su Segundo Parcial: "))
prom = (nota1 + nota2) /2

if nota1 and nota2 >= 7:
	print(f"Usted Promociono! Su promedio es de {prom}")
elif nota1 and nota2 >= 4:
	print(f"Usted quedo Regular, Su promedio es de {prom}")
elif nota1 and nota2 == -4:
	print(f"Usted desaprobo, su promedio es de {prom} , esta en condicion de libre")
