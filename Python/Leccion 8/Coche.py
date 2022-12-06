"""Definir una clase padre llamada coche y 2 clases hijas llamadas
    Moto y Bicicleta , las cuales heredan de la clase padre Coche.La clase
    padre debe tener los siguientes atributos y metodos:
    
    coche(clase padre)
    -Atributos(Color,ruedas)
    -Metodos(__init__() y __str__())
    
    Moto(clase hija de coche)
    -Atributos(velocidad(km/hr))
    -Metodos(__init__() y __str__())
    
    Bicicleta(clase hija de Coche)
    -Atributos(tipo(urbana/montaña/etc))
    -Metodos(__init__() y __str__())
    
    Crear un objeto de cada clase

    """
class Vehiculo:
    def __init__(self , color , ruedas) -> None:
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "[Color " + self.color  + "[Ruedas " +  str(self.ruedas) +  "]"  

class Moto(Vehiculo):
    def __init__(self, color, ruedas ,velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + "Velocidad(km/h)" + str(self.velocidad) # Pasamos a string velocidad por la funcion

class Bicicleta(Moto):
    def __init__(self, color, ruedas, velocidad , tipo) -> None:
        super().__init__(color, ruedas, velocidad)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + "    Tipo " + self.tipo

vehiculo1 = Vehiculo("Rojo" , 5)
print(vehiculo1)
moto1 = Moto("Negro" , 4 , 200)
print(moto1)
bicicleta1 = Bicicleta("Marron" , 5 , 200 ,"De carrera")
print(bicicleta1)