def main():
    cantidad_asignaturas = int(input("Ingrese la cantidad de asignaturas que desea ingresar: "))
    asignaturas = []
    
    for i in range(0, cantidad_asignaturas):
        asignatura = input(f"Ingrese el nombre de la asignatura {i + 1}: ")
        nota = float(input(f"Ingrese la nota de la asignatura {asignatura} (1.0 - 7.0): "))

        #asignaturas.append(asignatura)
        
        if (nota < 4.0):
            asignaturas.append(asignatura)


    print(asignaturas)
    return asignaturas

if __name__ == '__main__':
    main()