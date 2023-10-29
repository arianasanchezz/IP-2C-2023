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

# Ejercicio 1.4
def ordenados(s:[int]) -> bool:
    res: bool = True

    for i in range(0, len(s)-1, 1):
        if s[i] > s[i+1]:
            res = False

    return res

# Ejercicio 1.5
def alguna_palabra_larga(s:[str]) -> bool:
    i: int = 0
    condicion: bool = False

    while i < len(s) and not (condicion == True):
        if len(s[i]) > 7:
            condicion = True

        i += 1
        
    return condicion

# Ejercicio 1.6
def esPalindromo(texto: str) -> bool:
    textoSinEspacios = texto.replace(" ", "")
    textoModificado = textoSinEspacios.lower()

    return textoModificado == textoModificado[::-1]

#print(esPalindromo("anilina"))
#print(esPalindromo("Esto no es palindromo"))
#print(esPalindromo("Anita lava la tina"))

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
    
# Ejercicio 1.8
def saldo_actual_banco(historial: list[tuple[str, float]]) -> float:
    saldo_actual: float = 0
 
    for tupla in historial:
        if tupla[0] == "I":
            saldo_actual += tupla[1]

        if tupla[0] == "R":
            saldo_actual -= tupla[1]
    
    return saldo_actual

#transacciones = [("I", 2000),("R", 20),("R", 1000),("I", 300)]
#print(saldo_actual_banco(transacciones))

# SEGUNDA PARTE
# EJERCICIO 2
# Ejercicio 2.1 (*)
def cero_en_posiciones_pares(s:[int]) -> None:
    for i in range(0,len(s),2):
        s[i] = 0
    
    return s

# Ejercicio 2.2
def cero_en_posiciones_pares_in(s:[int]) -> [int]:
    nueva_lista: [int] = []
    i: int = 0

    while i < len(s):
        if (i % 2 == 0):
            nueva_lista.append(0)
        else:
            nueva_lista.append(s[i])
        i += 1

    return nueva_lista

# Ejercicio 2.3
def sinVocales(texto: str):
    vocales = ['a', 'e', 'i', 'o', 'u']
    nuevoTexto: str = ""

    for letra in texto:
        if letra not in vocales:
            nuevoTexto += letra
    
    return nuevoTexto

#print(sinVocales("hola"))

# Ejercicio 2.4
def reeemplazaVocales (texto: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    nuevoTexto: str = ""

    for letra in texto:
        if letra not in vocales:
            nuevoTexto += letra
        else:
            nuevoTexto += '_'

    return nuevoTexto

#print(reeemplazaVocales("hola"))

# Ejercicio 2.5
def daVueltaStr(s: str) -> str:
    texto_invertido: str = s[::-1]

    return texto_invertido

#print(daVueltaStr("hola"))

# Ejercicio 2.6
def eliminarRepetidos(s: str) -> str:
    sin_repetidos: str = ""

    for e in s:
        if not pertenece_1(sin_repetidos, e):
            sin_repetidos += e
    
    return sin_repetidos

#print(eliminarRepetidos("hoolaaaa"))

# EJERCICIO 3. Implementar una función para conocer el estado de aprobación de una materia a partir de las notas 
#              obtenidas por un/a alumno/a

# EJERCICIO 4
# Archivos separados

# EJERCICIO 5
# Ejercicio 5.1 (*)
def pertenece_a_cada_uno(s:[[int]], e: int) -> [bool]:
    i: int = 0
    res: [bool] = []

    while i < len(s):
        res.append(pertenece_3(s[i],e))
        i += 1
    
    return res

# Ejercicio 5.2
def esMatriz(s: [[int]]) -> bool:
    res: bool = True
    
    if len(s) == 0:
        res = False
    
    primera_fila: [int] = s[0]
    for fila in s:
        if len(fila) != len(primera_fila) or len(primera_fila) == 0:
            res = False

    return res



# falta terminar ej5, ej3 y el último de ej4

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

# print(ordenados([1,2,3,4]))
# print(ordenados([5,3,2,1]))
# print(ordenados([1,2,4,3,5]))

# print(alguna_palabra_larga(["Hola","Que","Tal","Ornitorrinco","Messi"]))
# print(alguna_palabra_larga(["Hola","Que","Tal","Messi"]))

#mi_lista:[int] = [0,1,2,3,4]
#print("Antes de la función:", mi_lista)
#print("Aplicando la función:", cero_en_posiciones_pares_in(mi_lista))

#matrizValida = [[1,2,3],[3,2,1],[3,3,3]]
#matrizInvalida1 = [[],[1,2,3]]
#matrizInvalida2 = [[1,2,3],[]]
#matrizInvalida3 = [[]]
#matrizInvalida4 = [[1,2,3,4],[1,2,3]]
#matrizInvalida5 = [[1,2],[1,0,2],[2,1]]

#print(esMatriz(matrizValida))
#print(esMatriz(matrizInvalida1))
#print(esMatriz(matrizInvalida2))
#print(esMatriz(matrizInvalida3))
#print(esMatriz(matrizInvalida4))
#print(esMatriz(matrizInvalida5))