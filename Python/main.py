 # Empiezo con las notas desde el dia de hoy 27/09

 # FUNCIONES RECURSIVAS

from select import select


def factorial(numero):
    if numero == 0 or numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) #  Recursividad

resultado = factorial(3) # Lo hacemos en codigo duro
print(f"El factorial del numero 5 es :  {resultado}")    

#  4.10.22
# Creacion de clases

"""class Persona: #Creamos una clase
    def __init__(self): # El init es el constructor de la clase
        self.nombre = 'Juan'
        self.apellido = "Miguel"
        self.edad = 22

persona1= Persona()
print(persona1.nombre) # Constructor
print(persona1.edad)
print(persona1.apellido)"""

# Forma correcta 

class Persona: #Creamos una clase
    def __init__(self , nombre , apellido , edad): # El init es el constructor de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1= Persona( "matias", "diaz" , 22)
print(persona1.nombre) # Constructor
print(persona1.edad)
print(persona1.apellido)

# Los atributos son :caracteristicas
# Los metodos son : el comportamiento que van a tener los objetos(acciones)
# METODO = FUNCION