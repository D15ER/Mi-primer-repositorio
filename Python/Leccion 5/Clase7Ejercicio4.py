def calculadora_impuestos(pago_sin_impuestos , impuestos):
    pago_total = pago_sin_impuestos + pago_sin_impuestos * (impuestos/100)
    return pago_total

pago_sin_impuestos = float(input("\nIndicar el precio: "))
impuestos = float(input("\nIndicar el impuesto en porcentaje: "))

print(f"\n\nSu total a pagar es de: {calculadora_impuestos(pago_sin_impuestos , impuestos )}")
