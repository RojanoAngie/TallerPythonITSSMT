from typing import List

if __name__ == '__main__':
    #Lista tipada incluida a partir de phtin 3. 5
    lista_Tipada : List[int] = [5, 12, 25, 33, 47, 63, 77, 82,91]


    lista_Tipada.append(10000)
    print("imprimiendo de forma tradicional")

    for elemento in lista_Tipada:
       print(elemento, end=" ")