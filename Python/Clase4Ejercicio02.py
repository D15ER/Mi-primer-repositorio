lista = list(range (1,11))

print(lista)
multiplicador = int(input('\nIndicar por que numero quiere multiplicar la lista: '))

for i in enumerate(lista):
    lista[i] *= multiplicador

print(lista)