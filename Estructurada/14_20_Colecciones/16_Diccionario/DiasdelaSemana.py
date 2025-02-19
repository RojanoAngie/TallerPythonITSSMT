def dia_de_la_semana (numero_dia:int) ->str:
    dias_semana={1:"Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "sabado", 7: "Domingo"}
  #  return dias_semana[numero_dia]#causaria un bug
    return dias_semana.get(numero_dia, "dia no valido") #es el mismo quede arriba, BUSQYEDA, pero como excepcion

if __name__ == '__main__':
    numero =3
    print(dia_de_la_semana(numero))