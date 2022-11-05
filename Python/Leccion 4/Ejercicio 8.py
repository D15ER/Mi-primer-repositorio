from ast import Break



saldo = 1000
salir = False


def menu():
    print("\nBienvenidos a Banelco")
    print("\nEste es nuestro Menu")
    print("\n1.Ingresar dinero en la cuenta\n2.Retirar dinero de la cuenta\n3.Mostrar dinero disponible\n4.Salir\n")




while not salir:

    menu()
    accion = int(input("Que accion desea tomar? "))
    if accion == 1:
        ingreso = int(input("\nIndique la cantidad de dinero que desea ingresar: "))
        saldo += ingreso
        
    if accion == 2:
        retiro = int(input("\nIndique la cantidad de dinero que quiera retirar: "))
        saldo -= retiro
        
    if accion == 3:
        print(f"\n\nSaldo de la cuenta: {saldo}")
        
    if accion == 4:
        print("\n\n\nFin del Programa")
        salir = True
        
