import saludos

def main():
    nombre = input("Ingrese su nombre: ")
    print(saludos.hola(nombre))
    print(saludos.adios(nombre))
    
main()
