import math

a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

discriminante = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)

print(f"Las raíces son: {raiz1} y {raiz2}")
