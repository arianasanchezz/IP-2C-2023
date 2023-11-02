# SIMULACRO PARCIAL
# Ejercicio 2
def elementos_exclusivos(s: list, t: list) -> list:
    res: list = []

    for elem in s:
        if not elem in t and not elem in res:
            res.append(elem)

    for elem in t:
        if not elem in s and not elem in res:
            res.append(elem)

    return res

s = [-1, 4, 0, 4, 3, 0, 100, 0, -1, -1]
t = [0, 100, 5, 0, 100, -1, 5]

print(elementos_exclusivos(s, t))