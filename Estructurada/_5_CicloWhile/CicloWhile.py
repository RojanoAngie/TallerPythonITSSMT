if __name__ == '__main__':
    print ("Este programa clacula la potencia de x a la y")
    x=int (input("proporciona el valor de la base "))
    y=int (input("proporciona el valor de lapotencia "))

    i=1; resultado= 1;
    while i<=y:
        print(f"conteo {i}")
        resultado *=x #acumulador
        i+=1

    print(f"el resultado de {x} a la potencia {y} es {resultado}")
