# EJERCICIO 2
def mezclar_cartas(s1: list, s2: list) -> list:
    res: list = []

    for i in range(0, len(s1), 1):
        res.append(s1[i])
        res.append(s2[i])

    return res

s1 = [1, 0, 4, 3]
s2 = [2, 5, 3, 1]

print(mezclar_cartas(s1, s2))