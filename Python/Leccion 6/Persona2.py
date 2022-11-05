class Persona2:
    def __init__(self , nombre , apellido , edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
# El guian bajo indica una encapsulacion
# La encapsulacion indica que los parametros no deberian de ser modificados

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes : {self.edad} , {self.apellido} ,{self.nombre}")

    @property # Decorador : necesita el metodo getter
    def nombre(self): # Metodo getter
        print("Estamos usando el metodo Get")
        return self.nombre

    @property
    def edad(self):
        print("Estamos usando el metodo get")
        return self.edad

    @property
    def apellido(self):
        return self.apellido
    
    @edad.setter
    def edad(self,edad):
        print("Estamos utilizando el metodo set")
        self.edad = edad

    @nombre.setter # Metodo setter
    def nombre(self,nombre):
        print("Estamos utilizando el metodo set")
        self.nombre = nombre
    
    @apellido.setter
    def apellido(self,apellido):
        self.apellido = apellido

    

Persona2("Ariel", "Josecpaz" , 22)

print(Persona2.nombre)

# Tarea crear 3 objetos mas utilizando los metodos getters and setters
# Para modicar y mostrar los cambios
