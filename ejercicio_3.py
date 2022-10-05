def main():
    cadena = input("Ingrese una cadena de texto: ")

    echo = cadena.split("salir")[0]

    print(echo)
    
    return echo

if __name__ == '__main__':
    main()