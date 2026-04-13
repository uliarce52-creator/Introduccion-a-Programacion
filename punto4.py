def punto_4():
	numero = int(input(f"Ingrese un numero: "))
	numero2 = int(input(f"Ingrese un numero: "))
	if numero > numero2:
		print(f"El {numero} es mayor que {numero2}")
	elif numero2 > numero:
		print(f"El {numero2} es mayor que {numero}")
	if numero == numero2:
		print(f"Ambos numeros son iguales")

punto_4()
