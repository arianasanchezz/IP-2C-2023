# EJERCICIO 4

def matriz_capicua(m: list[list]) -> bool:
    res: bool = True
    i: int = 0

    while i < len(m):
        fila_invertida = m[i][::-1]

        if m[i] != fila_invertida:
            res = False
        
        i += 1

    return res

m = [[1,0,0,1],[0,1,1,0],[5,3,3,5]]
m2 = [[1,0,0,1],[0,1,-1,0],[5,3,3,5]]

print(matriz_capicua(m))
print(matriz_capicua(m2))