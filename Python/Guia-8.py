from queue import LifoQueue as Pila
from queue import Queue as Cola

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

    while not p.empty():
        elem = p.get()

        if elem > maximo:
            maximo = elem
    
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

    while not p.empty():
        p.get()
        res += 1
    
    return res

print(cantidadDeElementos(p))


    

