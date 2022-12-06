class FiguraGeometrica:
    def __init__(self , ancho , alto):
        if self.validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("Valor incorrecto")
        if self.validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("Valor Incorrecto")

    #Encapsulacion
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        if self.validar_valores(ancho):
            self._ancho = ancho
    
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,alto):
        if self.validar_valores(alto):
            self._alto = alto

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}] [Alto: {self._alto}]"
    
    def validar_valores(self, valor): 
        # Metodo encapsulado
        return True if 0 < valor < 10 else False 