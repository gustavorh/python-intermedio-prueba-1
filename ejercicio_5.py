def main():
    valor = int(input("Ingrese el valor de la factura: "))
    iva = input("Ingrese el porcentaje de IVA a aplicar (0 a 100): ")

    factura_iva(valor, iva)

def factura_iva(valor, iva):
    if not iva:
        iva = 0
        iva = int(iva)
        
        iva = 19 / 100
        factura = valor + (valor * iva)
    else:
        iva = int(iva)
        print(f"IVA ingresado {iva}")
        iva = iva / 100
        factura = valor + (valor * iva)

    print(f"El valor de la factura original es de {valor}, aplicando un IVA de {iva * 100}%, el valor de la factura con IVA es de: {factura}")
    
    return factura
    
if __name__ == '__main__':
    main()