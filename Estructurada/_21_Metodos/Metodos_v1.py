def suma(x,y):
    suma=x+y #para convertir a string, solo pues ponerla conversion suma: str=str(x) +str(y)
    print(f"la suma de {x} + {y} es: {suma}")

if __name__ == '__main__':
    a=int(input("ingrese un numreo: "))
    b=int(input("ingrese otro numreo: "))

    suma(a, b)