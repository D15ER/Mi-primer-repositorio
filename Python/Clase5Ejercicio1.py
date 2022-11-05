a = int(input("Indique el primer valor del rango: "))
b = int(input("Indique el segundo valor del rango: "))


suma = 0

for i in range(a,b+1):
    if i % 2 == 0:
        suma += i
        
    
print(f"La suma de los numeros pares da:{suma} ")
