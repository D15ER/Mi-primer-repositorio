numero = int(input("\nIndique el numero: "))
lista =  []
j = 0

for i in range(0 , 11):
    j += 1
    lista.append(i * numero)  

print(lista)
