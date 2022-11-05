
lista = []

for i in range(0 , 51):
    if i <= 50:
        lista.append(i)

for i in lista:
    if i == 50:
        print(lista[i] , end='.')
    else:
        print(lista[i] , end= '-')