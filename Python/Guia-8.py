from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

# Guia 8


# Ejercicio 2 (*)
def clonarSinComentarios(nombre_archivo: str):
    archivo = (nombre_archivo, "r")
    destino = ('sinComentarios.py', "w")

    for linea in archivo.readlines():
        if linea.strip()[0] != "#":
            destino.write(linea)

    archivo.close()
    destino.close()

# clonarSinComentarios("archivo-comentado.py")

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

# Ejercicio 16.1

def armarSecuenciaDeBingo() -> Cola:
    lista: list = list(range(0,99))

    random.shuffle(lista)

    bolillero: Cola = Cola()

    for bolilla in lista:
        bolillero.put(bolilla)

    return bolillero

# Ejercicio 16.2

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