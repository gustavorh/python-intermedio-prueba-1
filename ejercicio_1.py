def main():
    print("Bienvenido! Por favor ingrese un número de teléfono con el siguiente formato:")
    print("prefijo-número-extensión, por ejemplo: +34-913724710-56")

    telefono = input("Ingrese un número de teléfono: ")
    solo_numero = telefono[4:-3]
    
    print(solo_numero)

    return solo_numero

if __name__ == '__main__':
    main()