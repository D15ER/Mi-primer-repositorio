lista = []

salir = False

while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

print(lista)
lista.sort() # La lista se ordena de mayo a menor con esta funcion

print(f'\nLista ordenada : \n{lista}')