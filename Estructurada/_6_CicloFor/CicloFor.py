import sys

if __name__ == '__main__':
    for i in range (10):
        print (f"{i}")

    print("---------------")
    for j in range (1,20):
        print (f"{j}", end =" ") # end=" " se usa para anular el salto de linea

    sys.stdout.write("Texto sin salto de Linea") #Funcion utilizada para imprimir npantalla sin salto de linea

    print("---------------")
    print("---------------")

    lista={1,2,3,4,5,6,7,8,9,10,11,12, 13,14, 15, 16}
    #una lista puede contener valores d edifeerente tipo, ademas una lista es mutable, es decir que se pueden agregar mas
    for elemento in lista:
        print(elemento)

    lista.add(200) #agregar elementos

    print("---------------")
    print("---------------")

    for elemento in lista:
        print(elemento)

