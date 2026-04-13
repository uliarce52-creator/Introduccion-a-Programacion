def maximo_minimo():
	n1 = int(input(f"Ingrese un numero: "))
	n2 = int(input(f"Ingrese un numero: "))
	n3 = int(input(f"Ingrese un numero: "))
	maximo = max(n1,n2,n3)
	minimo = min(n1,n2,n3)
	print(f"El numero mas grande es {maximo}")
	print(f"El numero mas chico es {minimo}")

maximo_minimo()
