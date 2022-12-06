from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica , Color):
    def __init__(self , lado_1 , lado_2, color):
        # Cuando hay diferentes padres , se inicializa de esta forma en vez de 
        # super.__init__(self ,lado)
        FiguraGeometrica.__init__(self , lado_1 , lado_2)
        Color.__init__(self,color)
    def calcular_area(self):
        return self.ancho * self.alto

    #Encapsulacion
    def __str__(self):
        return f"{FiguraGeometrica.__str__(self) } {Color.__str__(self)}"
        
        