def factorial(numero):  # funcion recursiva
    if numero >= 1:
        print(numero)
        factorial(numero-1)

factorial(5)