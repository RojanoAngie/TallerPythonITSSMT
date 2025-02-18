#Tarea 12 de Febrero del 2025
"""
   Una vez que conociste los tipos de datos de la categoría Collections de Python
   Ahora la tarea consiste en declarar una variabla para cada elemento, ingresa de forma manual, al menos 30 valores para cada elemento,
   y finalmente utiliza un for para imprimir cada uno de sus elementos en pantalla.
   Fecha límite de entrega: Lunes 17 de febrero del 2025

   ¡Éxito en esta actividad!
"""

"""
 Retroalimentación
    - No olvides que en Python es importante la indentación o bien los tabuladores.
    - Finalmente el resto del código está bien desarrollado y con esto puedes observar que 
    - Python es un lenguaje de programación fácil de usar.

Calificación: 9
"""

#Tarea 12 de Febrero del 2025
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, "seis", 7]  # list

    print("--------------------------------")
    print("lista: ")

for l in lista:
    print(l)

print("--------------------------------")
print("tupla: ")

tupla= (5,6,7,"ocho") #inmutable
for m in tupla:
    print(m)

print("--------------------------------")
print("conjunto: ")

conjunto = {9,10,"once", "doce"} # sepueden agregar listas
for c in conjunto:
    print(c)

print("--------------------------------")
print("diccionario: ")
diccionario = {"clave1": "valor1", "clave2": 20}
for d in diccionario:
    print(d)

