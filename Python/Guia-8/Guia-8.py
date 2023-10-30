from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# Guia 8 - Archivos, Pilas, Colas y Diccionarios
# Ejercicios hechos en clase práctica 23/10 marcados con un (*)

# PRIMERA PARTE - ARCHIVOS

# Ejercicio 1.1
def contar_lineas(nombre_archivo: str) -> int:
    archivo = open(nombre_archivo, "r", encoding='utf8')
    lineas = archivo.readlines()

    return len(lineas)

#print(contar_lineas('himno.txt'))

# Ejercicio 1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo = open(nombre_archivo, "r")
    res: bool = False
    lineas = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()
        if palabra in palabras:
            res = True
        
    return res
    
#print(existe_palabra("pueblo", "himno.txt"))
#print(existe_palabra("chileno", "himno.txt"))

# Ejercicio 1.3
def cantidad_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo = open(nombre_archivo, "r")
    res: int = 0
    lineas = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()
        
        for i in range(0, len(palabras), 1):
            if palabra == palabras[i]:
                res += 1
    
    return res

# print(cantidad_apariciones("himno.txt", "gloria"))            -tiene un error

# Ejercicio 2 (*)
def clonarSinComentarios(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    destino = open('sinComentarios.py', "w")

    for linea in archivo.readlines():
        if linea.strip()[0] != "#":
            destino.write(linea)

    archivo.close()
    destino.close()

# clonarSinComentarios("archivo-comentado.py")

# Ejercicio 3
def texto_reverso(nombre_archivo: str):
    archivo = open(nombre_archivo, "r")
    archivoDestino = open('reverso.txt', "w")
    lineas = archivo.readlines()

    for linea in lineas:
        pass

# Ejercicio 10 (*)
def buscarElMaximo(p: Pila) -> int:
    maximo = p.get()
    paux: Pila = Pila()

    while not p.empty():
        elem = p.get()

        if elem > maximo:
            maximo = elem
        paux.put(elem)

    while not paux.empty():
        elem = paux.get()
        p.put(elem)
    
    return maximo

p = Pila()
p.put(1)
p.put(2)
p.put(45)
p.put(80)
p.get()
p.get()
p.put(12)
p.put(1)
#print(buscarElMaximo(p))

def cantidadDeElementos(p: Pila) -> int:
    res: int = 0
    paux: Pila = Pila()

    while not p.empty():
        elem = p.get()
        paux.put(elem)
        res += 1
    
    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

#print(cantidadDeElementos(p))

# Ejercicio 16.1 (*)

def armarSecuenciaDeBingo() -> Cola:
    lista: list = list(range(0,99))

    random.shuffle(lista)

    bolillero: Cola = Cola()

    for bolilla in lista:
        bolillero.put(bolilla)

    return bolillero

# Ejercicio 16.2 (*)

def jugar_carton_de_bingo(carton: [int], bolillero: Cola) -> int:
    cantidadSinMarcar: int = 0
    jugadas: int = 0
    bolilleroAux: Cola = Cola()

    while cantidadSinMarcar > 0:
        numero: int = bolillero.get()
        bolilleroAux.put(numero)

        if numero in carton:
            cantidadSinMarcar -= 1
        jugadas += 1

    while not bolillero.empty():
        numero: int = bolillero.get()
        bolilleroAux.put(numero)
    
    while not bolilleroAux.empty():
        numero: int = bolilleroAux.get()
        bolillero.put(numero)

    return jugadas

# Ejercicio 19 (*)

def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo = open(nombre_archivo, "r")
    d = dict()
    lineas = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud in d:
                d[longitud] += 1

            else:
                d[longitud] = 1
    
    archivo.close()

    return d

# Ejercicio 21 (*)
def laPalabraMasFrecuente(nombre_archivo: str) -> str:
    archivo = open(nombre_archivo, "r")
    d = dict()
    lineas = archivo.readlines()

    for linea in lineas:
        palabras = linea.split()

        for palabra in palabras:
            if palabra in d:
                d[palabra] += 1
            
            else:
                d[palabra] = 1

    frecuencia_max: int = 0
    palabra_max: str

    for palabra, frecuencia in d.items():
        if frecuencia > frecuencia_max:
            frecuencia_max = frecuencia
            palabra_max = palabra

    return palabra_max

# print(laPalabraMasFrecuente('himno.txt'))
