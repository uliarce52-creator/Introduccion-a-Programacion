# TP VII - Ejercicio 7
# Menú interactivo que se repite hasta elegir "Salir"

import os

opcion = 0

while opcion != 4:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("********* MI PROGRAMA *********")
    print("1. Saludar.")
    print("2. Informar temperatura.")
    print("3. Mostrar nombre de materia.")
    print("4. Salir.")
    
    opcion = int(input("Seleccione una opción [1-4]: "))
    
    if opcion == 1:
        print("\n¡Hola! Bienvenido al programa.")
    elif opcion == 2:
        print("\nLa temperatura actual es de 22°C.")
    elif opcion == 3:
        print("\nMateria: Introducción a la Programación - UNLu")
    elif opcion == 4:
        print("\nHasta luego.")
    else:
        print("\nOpción inválida. Intente nuevamente.")
    
    if opcion != 4:
        input("\n[PRESIONE ENTER PARA CONTINUAR]")

