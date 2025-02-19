from statistics import mean

if __name__ == '__main__':
    materias=["Español", "matematicas", "fisica", "Quimica", "Computacion "]
    calificaciones=[]

    nombre = input("escribe tu nombre: ")

    for asignatura in materias:
        calif=float(input(f"dame la calificacion de {asignatura} : "))
        calificaciones.append(calif)

    prom= mean(calificaciones)
    print(f"el promedio de {nombre} es: {round(prom, 1)}") #round quitar decimales