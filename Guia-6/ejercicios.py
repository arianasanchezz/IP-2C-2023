import math

#  EJERCICIOS HECHOS EN CLASE PRACTICA 2/10
# Ejercicio 1.1
def imprimir_hola_mundo():
    print("¡Hola mundo!")

# Ejercicio 1.5
def perimetro() -> float:
    res:float = 2*math.pi
    return res

# Ejercicio 2.4
def es_multiplo_de(n:int, m:int) -> bool:
    if ((n%m) == 0):
        return True
    else:
        return False
    
# Ejercicio 3.3
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# Ejercicio 5.1
def devolver_el_doble_si_es_par(numero:int) -> int:
    if ((numero%2 == 0)):
        return 2*numero
    else:
        return numero

# Ejercicio 6.2
def imprimir_pares():
    i: int = 10
    while (i<=40):
        if (es_multiplo_de(i, 2)):
            print(i)
        i += 1

# Ejercicio 6.4
def cuenta_regresiva(n: int):
    while (n>=1):
        print(n)
        n -= 1
    print("Despegue")

# Ejercicio 7.2
def imprimir_pares2():
    for contador in range(10,41,2):
        print(contador)

# Ejercicio 7.4
def cuenta_regresiva2(n: int):
    for i in range(n,0,-1):
        print(i)
    print("Despegue")



# imprimir_hola_mundo()
# print(perimetro())
# print(es_multiplo_de(4,2))
# print(es_multiplo_de(5,2))
# print(es_nombre_largo("Mariana"))
# print(es_nombre_largo("Marianela"))
# print(devolver_el_doble_si_es_par(2))
# print(devolver_el_doble_si_es_par(3))
# imprimir_pares()
# cuenta_regresiva(10)
# imprimir_pares2()
# cuenta_regresiva2(10)