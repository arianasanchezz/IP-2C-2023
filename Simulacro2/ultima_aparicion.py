# SIMULACRO PARCIAL
# Ejercicio 1
def ultima_aparicion(s: list, e: int) -> int:
    res: int = 0
    i: int = 0

    while i < len(s):
        if e == s[i]:
            res = i
        
        i += 1

    return res

s = [-1, 4, 0, 4, 100, 0, 100, 0, -1, -1]
e = 0

print(ultima_aparicion(s, e))