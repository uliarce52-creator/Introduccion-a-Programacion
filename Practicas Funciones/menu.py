# MENU CALCULADORA

from CALCU import *

def ingreso_numeros():
	num1 = int(input(f"Ingrese un numero: "))
	num2 = int(input(f"Ingrese un numero: "))
	return num1, num2
	
def mostrar_menu():
	print("----- CALCULADORA-----")
	print("1. SUMA")
	print("2. RESTA")
	print("3. MULTIPLICAR")
	print("4. DIVIDIR")
	print("0. SALIR")
	opcion = int(input(f"Ingrese Opcion: "))
	return opcion
	
def procesar_menu(opcion):
	if opcion == 1:
		num1, num2 = ingreso_numeros()
		print(suma(num1, num2))
	elif opcion == 2:
		num1, num2 = ingreso_numeros()
		print(resta(num1,num2))
	elif opcion == 3:
		num1, num2 = ingreso_numeros()
		print(multi(num1,num2))
	elif opcion == 4:
		num1, num2 = ingreso_numeros()
		print(dividir(num1,num2))
	else:
		print("Opcion invalida")
		
while (opcion := mostrar_menu()) != 0:
	procesar_menu(opcion)
