
def multiplicar_valores(*args): # Aca indica un argumento , se puede llamar de la forma que nosotros queramos
    resultado = 1 # Todo numero multilpicado por 0 es 0
    for numero in args:
        resultado *= numero
    return resultado


print(f"Su multiplicacion es: {multiplicar_valores(1,2,3,4,5,6,7,8)}")