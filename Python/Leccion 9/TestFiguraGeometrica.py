from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creacion de objeto clase Cuadrado".center(50, "_"))
cuadrado1 = Cuadrado( 1,3 , "Azul")
cuadrado1.alto = -10 # No se modifica ya que no dentro de los parametros adecuados
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f"Calculo del area del cuadrado: {cuadrado1.calcular_area()}")

# METODO MRO = Method Resolution Order

print(Cuadrado.mro())

# Encapsulacion
print(cuadrado1)

print("Creacion de objeto clase Rectangulo".center(50, "_"))
rectangulo1 = Rectangulo(2 , 2 , "rojo")

print(rectangulo1.ancho)
print(rectangulo1.alto)
print(f"Calculo del area del rectangulo: {rectangulo1.calcular_area()}")

#Encapsulacion 
print(rectangulo1)