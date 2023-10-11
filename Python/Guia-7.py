# Guia 7 - Funciones sobre listas (tipos complejos)
#  EJERCICIOS HECHOS EN CLASE PRACTICA 9/10 MARCADOS CON UN (*)

# PRIMERA PARTE
# EJERCICIO 1
# Ejercicio 1.1 (*)
def pertenece_1(s:[int], e:int) -> bool:
    return e in s

def pertenece_2(s:[int], e:int) -> bool:
    pertenece: bool = False
    i: int = 0
    while (i < len(s)) and (not pertenece):
        if s[i] == e:
            pertenece = True
        i += 1

    return pertenece
    
def pertenece_3(s:[int], e:int) -> bool:
    res: bool = False
    
    for i in range(0, len(s),1):
        if s[i] == e:
            res = True
    
    return res

# Ejercicio 1.2
def divide_a_todos(s:[int], e:int) -> bool:
    condicion: bool = True
    i: int = 0
    while i < len(s):
        if s[i] % e != 0:
            return False
        i += 1
    return condicion

# Ejercicio 1.3 (*)
def suma_total(s:[int]) -> int:
    res: int = 0
    i: int = 0

    while i < len(s):
        res += s[i]
        i += 1
    
    return res

# Ejercicio 1.7 (*)
def es_un_numero(caracter:str) -> bool:
    return (caracter <= '9') and (caracter >= '0')

def tiene_un_numero(contraseña: str) -> bool:
    i: int = 0
    vale_condicion: bool = False

    while (i < len(contraseña)) and not (es_un_numero(contraseña[i])):
        i += 1
    vale_condicion: bool = i < len(contraseña)
    
    return vale_condicion

def es_mayuscula(caracter: str) -> bool:
    return (caracter >= 'A') and (caracter <= 'Z')

def tiene_una_mayuscula(contraseña: str) -> bool:
    i: int = 0
    vale_condicion: bool = False

    while (i < len(contraseña)) and not (es_mayuscula(contraseña[i])):
        i += 1
    vale_condicion: bool = i < len(contraseña)

    return vale_condicion

def es_minuscula(caracter: str) -> bool:
    return (caracter >= 'a') and (caracter <= 'z')

def tiene_una_minuscula(contraseña: str) -> bool:
    i: int = 0
    vale_condicion: bool = False

    while (i < len(contraseña) and not (es_minuscula(contraseña[i]))):
        i += 1
    vale_condicion: bool = i < len(contraseña)

    return vale_condicion

def fortaleza(contraseña: str) -> str:
    if len(contraseña) > 8 and (tiene_un_numero(contraseña)) and (tiene_una_mayuscula(contraseña) and (tiene_una_minuscula(contraseña))):
        return "VERDE"
    if len(contraseña) < 5:
        return "ROJA"
    else:
        return "AMARILLA"

# SEGUNDA PARTE
# EJERCICIO 2
# Ejercicio 2.1 (*)
def cero_en_posiciones_pares(s:[int]) -> None:
    for i in range(0,len(s),2):
        s[i] = 0
    
    return s

# EJERCICIO 5
# Ejercicio 5.1 (*)
def pertenece_a_cada_uno(s:[[int]], e: int) -> [bool]:
    i: int = 0
    res: [bool] = []

    while i < len(s):
        res.append(pertenece_3(s[i],e))
        i += 1
    
    return res


# print(suma_total([1,2,3,60]))
# print(pertenece_3([1,2,3],4))
# print(pertenece_3([1,2,3,4],4))
# print(pertenece_2([1,2,3],4))
# print(pertenece_2([1,2,3,4],4))
# print(es_un_numero('2'))
# print(es_un_numero('A'))
# print(tiene_un_numero('hola'))
# print(tiene_un_numero('hola4as'))
# print(tiene_una_mayuscula('hola'))
# print(tiene_una_mayuscula('Hola'))
# print(tiene_una_minuscula('HOLA'))
# print(tiene_una_minuscula('HOLa'))

#print(fortaleza("Contraseña123"))
#print(fortaleza("contraseña123"))
#print(fortaleza("123"))
#print(fortaleza("holA"))
#print(fortaleza("Contraseña"))
#print(fortaleza("123456789"))

# mi_lista:[int] = [0,1,2,3,4]
# print("Antes de la función:", mi_lista)
# cero_en_posiciones_pares(mi_lista)
# print("Después de la función:", mi_lista)

# print(pertenece_a_cada_uno([[2,3],[1],[0,0,0],[],[1,2]], 2))

#print(divide_a_todos([2,4,6],3))
#print(divide_a_todos([10,25,40],5))