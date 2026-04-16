tabla = int(input(f"Ingrese el numero de la tabla: "))
num = 0

while (num <= tabla):
	j = 0
	while (j <= 10):
		print( str(num) + " * " + str(j) + " = " + str(num * j))
		j += 1
	num +=1
	print()
