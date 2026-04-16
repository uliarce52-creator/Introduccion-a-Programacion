def buclewhile():
	tabla = int(input(f"Ingrese el numero de la tabla que quiera ver: "))
	num = 1
	
	while (num <= tabla):
		j = 1
		while (j <= tabla):
			print(str(num) + " * " + str(j) + " = " + str(num * j))
			j += 1
			num += 1
		print()

buclewhile()
