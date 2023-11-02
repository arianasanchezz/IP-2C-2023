# SIMULACRO PARCIAL
# Ejercicio 4
def convertir_a_diccionario(lista: list) -> dict:
    res: dict = dict()

    for elem in lista:
        if elem in res:
            res[elem] += 1
        else:
            res[elem] = 1

    return res

lista = [-1, 0, 4, 100, 100, -1, -1]
print(convertir_a_diccionario(lista))