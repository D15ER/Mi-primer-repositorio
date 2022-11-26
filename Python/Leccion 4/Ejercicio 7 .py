import random


aleatorio = random.randint(0,100) 
contador= 0
salir = False
while not salir:
    numero = int(input("\nIndicar el numero a adivinar: "))
    contador += 1
    if numero ==  aleatorio:
        print("Felicidades, adivinaste el numero")
        print(f"\n\nEl numero aleatorio era {aleatorio}")
        print(f"\n\nY la cantidad de intentos fueron: {contador}")   
        salir = True
    elif  numero < aleatorio:
        print("\n\nProbar nuevamente, el numero tiene que ser mas alto")
    elif numero > aleatorio:
        print("\n\nProbar nuevamente, el numero tiene que ser mas bajo")
    