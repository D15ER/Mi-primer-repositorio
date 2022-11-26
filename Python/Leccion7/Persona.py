
class Persona:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

@property
def edad(self):
    return self._edad
@edad.setter
def edad(self, edad):
    self._edad = edad

@property 
def nombre (self):
    return self._nombre

@nombre.setter
def nombre (self):
    self._nombre = nombre

def __str__(self): # Override == Sobrescribir
    return f"Persona:  {self._nombre} {self._edad}"

class Empleado(Persona): #Empleado es una subclase de Persona
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad) # Es el constructor de la clase objet
        self.sueldo = sueldo

@property
def sueldo(self):
    return self._sueldo

@sueldo.setter
def sueldo (self):
    self._sueldo = sueldo

def __str__(self): # Override == Sobrescribir
    return f"Empleado: [Sueldo{self._sueldo} {super().__str__()}]"


empleado1 = Empleado("Matias",40,321321321)
print(empleado1.nombre) #Indicmos la variable que queremos llamar
print(empleado1.edad)
print(empleado1.sueldo)

empleado2 = Empleado("Jose Miguel" , 32 , 132231321)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
