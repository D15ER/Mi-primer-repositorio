
class Persona:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona): #Empleado es una subclase de Persona
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad) # Es el constructor de la clase objet
        self.sueldo = sueldo

empleado1 = Empleado("Matias",40,321321321)
print(empleado1.nombre) #Indicmos la variable que queremos llamar
