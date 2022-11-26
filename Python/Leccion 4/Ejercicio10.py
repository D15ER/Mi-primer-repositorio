cadena = input("Indicar una cadena: ")
lista = []

for i in cadena:
    if i not in lista: # Si el caracter aun no esta en la lista
        lista.append(i) # Se agrega a  lista
    
print(f'\nLista de caracteres sin repetir :{lista}')

#Hacer un programa que pida una cadena por teclado
# y meter los caracteres en una lista sin repetirlos