# EJERCICIO 1
def ind_nesimo(s: list, n: int, elem: int) -> int:
    res: int = -1
    cantidad_de_apariciones: int = 0
    ultima_aparicion: int = 0

    for i in range(0, len(s), 1):
        if s[i] == elem:
            cantidad_de_apariciones += 1
            ultima_aparicion += 1

            if cantidad_de_apariciones == n:
                res = ultima_aparicion
    
    return res

s = [-1, 1, 1, 3, 1, 5, 4]
n = 2
elem = 1

print(ind_nesimo(s, n, elem))