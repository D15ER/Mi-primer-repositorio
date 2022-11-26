class Persona2:
    def __init__(self , nombre , apellido , edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
# El guian bajo indica una encapsulacion
# La encapsulacion indica que los parametros no deberian de ser modificados

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes : {self._nombre} , {self._apellido} ,{self._edad}")

    @property # Decorador : necesita el metodo getter
    def nombre(self): # Metodo getter
        print("Estamos usando el metodo Get")
        return self._nombre
    
    @nombre.setter # Metodo setter
    def nombre(self,nombre):
        print("Estamos utilizando el metodo set")
        self._nombre = nombre

    @property
    def edad(self):
        print("Estamos usando el metodo get")
        return self._edad

    @edad.setter
    def edad(self,edad):
        print("Estamos utilizando el metodo set")
        self._edad = edad

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    def __del__(self): # Generamos el metodo destructor
        print(f"Persona2: {self._nombre} {self._apellido} {self._edad}")

    
if __name__ == "__main__": # Esto nos sirve para que en otros archivos no ejecutemos todo junto
    Persona1 = Persona2("Ariel", "Josecpaz" , 22)

    print(Persona1.nombre) # Llamamos al metodo Getter
    Persona1.nombre = "Matias" # Asignamos un nuevo valor y utilizamos el metodo set
    print(Persona1.nombre) # Llamamos al metodo Getter
    print(Persona1.mostrar_detalles())

    print(__name__) # Nos indica donde se esta ejecutando


# Tarea crear 3 objetos mas utilizando los metodos getters and setters
# Para modicar y mostrar los cambios
