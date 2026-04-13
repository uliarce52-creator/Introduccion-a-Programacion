dividendo = float(input(f"Ingrese el numero: "))
denominador = int(input(f"Ingrese su denominador: "))
div = dividendo / denominador

if denominador == 0:
	print(f"Cuenta nula! No se puede poner 0 (cero) como denominador!")
else:
	print(f"El resultado de su cuenta es {div}")
