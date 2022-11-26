from Persona2 import Persona2
print("Creacion de objetos".center(50 , "_"))
if __name__ == "__main__":
    Persona5 = Persona2("Matias" , "Diaz" , 22)
    Persona5.mostrar_detalles()
    print(__name__)

print("Eliminacion de Objetos".center(50,"_"))

del Persona5
