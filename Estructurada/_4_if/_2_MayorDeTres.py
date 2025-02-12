if __name__ == '__main__':
    a=int(input("Ingrese el primer numero"))
    b=int(input("Ingrese el segundo numero"))
    c=int(input("Ingrese el tercer numero"))

    if a>b:
        if a>c:
            print(" El mayor es: ",a )

        else:
            print(" El mayor es: ", b)
    elif b>c:
        print (f"El mayor es {b}")
    else:
        print(f"El mayor es {c}")