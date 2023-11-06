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

# print(cantidad_apariciones("himno.txt", "gloria"))           # *tiene un error

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
    lineas_al_reves = lineas[::-1]

    for linea in lineas_al_reves:
        archivoDestino.write(linea)

    archivo.close()
    archivoDestino.close()

# texto_reverso("himno.txt")

# Ejercicio 4
def agregar_al_final(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "a")
    archivo.write("\n" + frase + "\n")
    archivo.close()

# agregar_al_final("reverso.txt", "HIMNO NACIONAL ARGENTINO")

# Ejercicio 5
def agregar_al_principio(nombre_archivo: str, frase: str):
    archivo = open(nombre_archivo, "r")
    contenido_original = archivo.read()
    archivo.close()

    archivo = open(nombre_archivo, "w")
    archivo.write(frase + "\n" + contenido_original)
    archivo.close()

# agregar_al_principio("himno.txt", "HIMNO NACIONAL ARGENTINO")

# Ejercicio 6 - Implementar una función que lea un archivo en modo binario y devuelva la lista de palabras legibles (despues lo hago)

# Ejercicio 7 

# SEGUNDA PARTE - PILAS

# Ejercicio 8
def generar_nros_al_azar(n:int, desde: int, hasta: int) -> Pila:
    pila: Pila = Pila()

    for i in range(0, n):
        elem = random.randint(desde, hasta)
        pila.put(elem)

    return pila

# pila_nros_al_azar = generar_nros_al_azar(3, 1, 10)
# mi_lista = []
# mi_lista.append(pila_nros_al_azar.get())
# mi_lista.append(pila_nros_al_azar.get())
# mi_lista.append(pila_nros_al_azar.get())
# print(mi_lista)

p = Pila()
p.put(1)
p.put(2)
p.put(45)
p.put(80)
p.get()
p.get()
p.put(12)
p.put(1)
p.put(5)

# Ejercicio 9
def cantidad_elementos(p: Pila) -> int:
    res: int = 0
    paux: Pila = Pila()

    while not p.empty():
        elem = p.get()
        res += 1
        paux.put(elem)

    while not paux.empty():
        elem = paux.get()
        p.put(elem)

    return res

# print(cantidad_elementos(p))

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

# print(buscarElMaximo(p))

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

# Ejercicio 11
def esta_bien_balanceada(s: str) -> bool:
    pila_de_parentesis = Pila()

    for caracter in s:
        if caracter == "(":
            pila_de_parentesis.put(caracter)
        elif caracter == ")":
            if pila_de_parentesis.empty():
                return False
            pila_de_parentesis.get()
    
    return cantidad_elementos(pila_de_parentesis) == 0  #falta terminar

formula1 = "1 + ( 2 x 3 - ( 20 / 5 ) )"
formula2 = "10 * ( 1 + ( 2 * ( -1))"
formula3 = "1 + ) 2 x 3 ( ( )"
#print(esta_bien_balanceada(formula1))
#print(esta_bien_balanceada(formula2))
#print(esta_bien_balanceada(formula3))

# Ejercicio 12
def evaluar_expresion(expresion: str) -> int:
    tokens = expresion.split()
    operadores = ['+', '-', '*', '/']
    pila_de_operandos: Pila = Pila()

    for token in tokens:
        if token not in operadores:
            pila_de_operandos.put(int(token))

        elif token in operadores:
            operando2 = pila_de_operandos.get()
            operando1 = pila_de_operandos.get()
            res: int = 0
            
            if token == '+':
                res = operando1 + operando2
            elif token == '-':
                res = operando1 - operando2
            elif token == '*':
                res = operando1 * operando2
            elif token == '/':
                res = operando1 / operando2
            
            pila_de_operandos.put(res)

    return pila_de_operandos.get()

expresion = "3 4 + 5 * 2 -"
resultado = evaluar_expresion(expresion)
#print(resultado)                    # me salio :D


# TERCERA PARTE - COLAS

c = Cola()
c.put(1)
c.put(2)
c.put(3)
c.get()
c.put(4)
c.get()
c.put(5)
c.put(6)

# Ejercicio 13

# Ejercicio 14
def cantidad_elementos_C(c: Cola) -> int:
    res: int = 0
    c_aux: Cola = Cola()

    while not c.empty():
        elem = c.get()
        res += 1
        c_aux.put(elem)
    
    while not c_aux.empty():
        elem = c_aux.get()
        c.put(elem)

    return res

# print(cantidad_elementos_C(c))

# Ejercicio 15
def buscar_el_maximo_C(c: Cola) -> int:
    maximo: int = 0
    c_aux: Cola = Cola()

    while not c.empty():
        elem = c.get()
        if elem > maximo:
            maximo = elem
        c_aux.put(elem)

    while not c_aux.empty():
        elem = c_aux.get()
        c.put(elem)

    return maximo

# print(buscar_el_maximo_C(c))

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

# Ejercicio 17
def n_pacientes_urgentes(c: Cola[int, str, str]) -> int:
    pacientes_urgentes: int = 0

    while not c.empty():
        paciente = c.get()
        if paciente[0] >= 1 and paciente[0] <= 3:
            pacientes_urgentes += 1
    
    return pacientes_urgentes

guardia_hospital: Cola = Cola()
guardia_hospital.put([10, "Pepe", "General"])
guardia_hospital.put([2, "Fulano", "General"])
guardia_hospital.put([3, "Mengano", "General"])
guardia_hospital.put([7, "Menganito", "General"])
guardia_hospital.put([1, "Fulanito", "General"])

# print(n_pacientes_urgentes(guardia_hospital))

# Ejercicio 18
def a_clientes(c: Cola((str, int, bool, bool))) -> Cola((str, int, bool, bool)):
    cola_prioridad: Cola = Cola()
    cola_preferencial: Cola = Cola()
    cola_resto: Cola = Cola()

    while not c.empty():
        cliente = c.get()

        if cliente[3] == True:
            cola_prioridad.put(cliente)
        elif cliente[2] == True:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)

    cola_final: Cola = Cola()
    while not cola_prioridad.empty():
        cliente_con_prioridad = cola_prioridad.get()
        cola_final.put(cliente_con_prioridad)
    while not cola_preferencial.empty():
        cliente_preferencial = cola_preferencial.get()
        cola_final.put(cliente_preferencial)
    while not cola_resto.empty():
        cliente_comun = cola_resto.get()
        cola_final.put(cliente_comun)
    
    return cola_final

cola_ingreso = Cola()
cola_ingreso.put(("Alfre Montes de Oca", 12345678, True, True))
cola_ingreso.put(("Jazmin Badia", 98765432, False, False))
cola_ingreso.put(("German Beder", 56789012, True, False))
cola_ingreso.put(("Luquitas Rodríguez", 34567890, False, True))

cola_atencion = a_clientes(cola_ingreso)

while not cola_atencion.empty():
    cliente = cola_atencion.get()
#   print(f"Atendiendo a {cliente[0]} (DNI: {cliente[1]})")

# CUARTA PARTE - DICCIONARIOS

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

# Ejercicio 20 - Desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
         # usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás y hacia adelante en la historia de navegación.
         # Las claves del diccionario serán los nombres de usuario y los valores serán pilas

def visitar_sitio(historiales: dict, usuario: str, sitio: str):  # recibe el diccionario de historiales,
    if usuario in historiales:                                   # el nombre de usuario y el sitio web visitado. 
        historiales[usuario].put(sitio)               # agrega el sitio web al historial del usuario correspondiente.
    else:
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)

historiales_aux = {}        # creo un diccionario auxiliar para almacenar los sitios visitados recientemente al navegar atrás
def navegar_atras(historiales: dict, usuario: str):
    if usuario in historiales:
        visitado = historiales[usuario].get()
        if usuario not in historiales_aux:
            historiales_aux[usuario] = Pila()
        historiales_aux[usuario].put(visitado)

def navegar_adelante(historiales: dict, usuario: str):
    if usuario in historiales:
        visitado = historiales_aux[usuario].get()
        historiales[usuario].put(visitado)

historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_atras(historiales, "Usuario2")
navegar_adelante(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "twitter.com")
visitar_sitio(historiales, "Usuario1", "twitter.com")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_atras(historiales, "Usuario2")
navegar_atras(historiales, "Usuario1")
navegar_adelante(historiales, "Usuario2")

#for usuario, historial in historiales.items():
    #print(f"Historial de {usuario}: {list(historial.queue)}")

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

# print(laPalabraMasFrecuente("himno.txt"))
