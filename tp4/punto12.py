num1 = int(input(f"Introduce un numero: "))
num2 = int(input(f"Introduce otro numero: "))
num3 = int(input(f"Introduzca un ultimo numero: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
absoluto = abs(num1)

print(f"El numero de mayor valor es el {mayor}")
print(f"El numero de menor valor es el {menor}")
print(f"El valor absoluto del primer numero es {absoluto}")
