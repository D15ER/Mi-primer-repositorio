class MiClase:
    # Variable de clase , este atributo dara a cada objeto el mismo valor
    variable_clase = "Esta es una variable de clase"

    def __init__(self , variable_instancia) -> None:
        self.variable_instancia = variable_instancia

# Podemos acceder a la variable de clase por la misma clase
print(MiClase.variable_clase)

# Para pode acceder a la variable de instancia tenemos que crear el objeto miclase1
miclase1 = MiClase("Es es una variable de instancia")
print(miclase1.variable_instancia)
miclase2 = MiClase("Esta es la segundo prueba de la variable de instancia")
print(miclase2.variable_instancia)