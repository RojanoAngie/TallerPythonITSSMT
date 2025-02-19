def ListaPar (x : [ ]) -> [ ]:
    lista =[]
    for elemento in x:
        if elemento%2 == 0:
            lista.append(elemento)

    return lista

def ListaImpar(x: [ ]) -> [ ]:
    lista=[]
    for elemento in x:
        if elemento%2==1:
            lista.append(elemento)
    return lista

if __name__ == '__main__':
    miLista=[1,2,3,4,5,6,7,8,9,19,10,11,12]

    print(f"los pares son: {ListaPar(miLista)}")
    print(f"los impares son: {ListaImpar(miLista)}")
