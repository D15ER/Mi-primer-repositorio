numero = int(input("Digite un numero: ")) # Mientras el numero sea negativo


factorial = 1
for i in range(1,numero+1):
    factorial *=i

print(f"\nEl factorial del numero {numero} positivo ingreso es : {factorial}")