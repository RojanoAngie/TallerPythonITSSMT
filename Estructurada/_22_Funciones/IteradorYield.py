def contar_hasta (n) ->tuple[str, int]:
    count=1
    potencia=0
    while count <=n:
        potencia: int=count**2
        valor:str=f"valor {count}"
        yield(valor,potencia) #sirve para reflejar dos valores, o en est asoo una tupla como si feuese un return
        count +=1

if __name__ == '__main__':
    #usando la funvion yield
    for numero, potencia in contar_hasta(10):
        print(f"para el {numero} su potencia es {potencia}") #
        input("deteniednoel proceso") # de detiene el proceso dentro del for, fuera, sigue

