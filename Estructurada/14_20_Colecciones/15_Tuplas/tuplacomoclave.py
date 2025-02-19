if __name__ == '__main__':
    #usar un tupla como clave en un diccionario

    diccionario= {}

    #agregar tupla como clave
    diccionario[("Ana", 25)] ="Estudiante"
    diccionario[("LUis", 30)] ="Ingniero"
    diccionario[("Carlos", 40)] ="ABogado"

    #acceder a los valores del diccionario usando la tuplacomo clave
    ocupacionAna =diccionario[("Ana",25)]
    ocupacionLuis =diccionario[("LUis",30)]
    ocupacionCarlos =diccionario[("Carlos",40)]

#Busqueda
    print(f"Ana es {ocupacionAna}")
    print(f"Luis es {ocupacionLuis}")
    print(f"Carlos es {ocupacionCarlos}")
