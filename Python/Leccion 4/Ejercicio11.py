# Consultar por la linea 31
# por que el FOR considera que  valor y clave

Agenda = {}

while True:
    print("\n\n\tBienvenidos a su agenda")
    print("\n1.Agregar nuevo contacto")
    print("2.Borrar contacto")
    print("3.Ver contactos existentes")
    print("4.Salir")
    numero = int(input("Indicar la opcion"))
    if numero == 1:
       nombre = input("Digite el nombre del contacto: ")
       telefono = input("Digite el numero de telefono: ")
       if nombre not in Agenda:
            Agenda [nombre] = telefono
            print("\nEl contacto esta agregado exitosamente!")
       else:
            print("Ese nombre de contacto ya existe.")
    elif numero == 2:
        nombre = input("Cual es el nombre del contacto: ")
        if nombre in Agenda:
            del (Agenda[nombre]) # Se borra de la llave el valor
            print(" Se ha eliminado el contacto requerido.")
        else:
            print("No se ha encontrado el contacto.")
    elif numero == 3:
        print("Esta es su agenda")
        for clave , valor in Agenda.items():
            print(f"Nombre: {clave} , Telefono: {valor}")
    elif numero == 4:
        print("Gracias por utilizar su agenda de contacto.")
        break
    else:
        print("Indique un valor correcto.")  

print("\n\n")    