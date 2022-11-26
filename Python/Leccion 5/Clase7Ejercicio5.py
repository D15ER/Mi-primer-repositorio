def f_a_c(grados_f):
    grados_c = (grados_f - 32) * 0.5556
    return grados_c

def c_a_f(grados_c):
    grados_f = (grados_c * 1.8) + 32
    return grados_f

while True:
    print("image.png\n\nBienvenido a la calculadora temperaturas.")
    print("\n\n1_Calcular de grados Farenheint a Celcius\n2_Calcular de grados Celcius a Fahrenheit\n3_Salir")
    opcion = int(input("\nIndicar que opcion desea: "))
    if opcion == 1:
        grados_f = int(input("\nIndicar los grados Fahrenheit: "))
        print(f"\nF:{grados_f} == C:{f_a_c(grados_f)}")
    if opcion == 2:
        grados_c = int(input("\nIndicar los grados Celcius: "))
        print(f"\nC:{grados_c} == F:{c_a_f(grados_c)}")
    if opcion == 3:
        break
    else:
        print("\nIngrese un valor correcto.")
    
