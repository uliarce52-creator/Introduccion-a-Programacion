lado1 = float(input(f"Ingrese un numero: "))
lado2 = float(input(f"Ingrese el siguiente numero: "))
lado3 = float(input(f"Ingrese el ultimo numero: "))

if lado1 == lado2 == lado3:
	print(f"Su triangulo es Equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
	print("El triángulo es ISÓSCELES")
else:
	print(f"Su triangulo es Escaleno")
