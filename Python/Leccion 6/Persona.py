class Persona: # Creamos una clase
    def __init__(self , nombre , apellido , edad): # __init__ es el constructor del objeto
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Persona: {self.nombre} ,  {self.apellido} , {self.edad}") 
        #Dentro de una clase: para ingresar un valor de otro metodo usamos Self

persona1 = Persona("Matias" ,"Diaz de Otazu" , 22) #Indicamos los atributos

# Mostrar todas los atributos en una misma linea

""" print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)"""

print(f"El objeto 1 se llama {persona1.nombre} {persona1.apellido} y tiene {persona1.edad} años")

persona2= Persona("Jose maria" , "Listorti" , 52)
print(f"El objeto 2 se llama {persona2.nombre} {persona2.apellido} y tiene {persona2.edad} años")

# Los atributos son : caractaristicas
# Los metodos son: El comportamiento que van a tener los objetos
# Los metodos estan asociodas a una clase 

persona1.mostrar_detalle()