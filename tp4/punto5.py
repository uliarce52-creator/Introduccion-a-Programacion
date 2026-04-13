apellido = input(f"Ingrese su apellido: ")
nota1 = int(input(f"Ingrese la nota de su primer parcial: "))
nota2 = int(input(f"Ingrese la nota de su segundo parcial: "))
prom = (nota1 + nota2) // 2

print(f"Alumno {apellido}")
print(f"- Primer parcial: {nota1}")
print(f"- Segundo parcial: {nota2}")
print(f"- Promedio: {prom}")
