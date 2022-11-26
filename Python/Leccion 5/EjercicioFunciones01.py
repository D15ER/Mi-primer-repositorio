def matematicas(*args): # Indica que vamos a recibir una cantidad de parametros indefinidos
    resultado = 0
    for valor in args:
        resultado += valor
        
    return resultado
print(matematicas(50,1,2,54))