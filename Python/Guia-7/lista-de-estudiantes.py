# GUIA 7 - EJERCICIO 4 (programas interactivos con input)
# 1. Implementar una función para construir una lista con los nombres de mis estudiantes. La función solicitará al 
#    usuario los nombres hasta que ingrese la palabra “listo”. Devuelve la lista con todos los nombres ingresados.

def crear_lista_de_estudiantes():
    lista: [str] = []
    nombre_estudiante: str = ""

    while nombre_estudiante != "Listo":
        nombre_estudiante = str(input("Ingrese el nombre del alumno. 'Listo' para terminar: "))

        if nombre_estudiante != "Listo":        # agrego este if sino en la lista también imprime 'Listo'
            lista.append(nombre_estudiante)
    
    return lista

lista_de_estudiantes = crear_lista_de_estudiantes()

print("Lista de estudiantes ingresados:")
for estudiante in lista_de_estudiantes:
    print(estudiante)