import math

# Guía 6 - Introducción a Lenguaje Imperativo
#  EJERCICIOS HECHOS EN CLASE PRACTICA 2/10 MARCADOS CON UN (*)
# Ejercicio 1.1 (*)
def imprimir_hola_mundo():
    print("¡Hola mundo!")

# Ejercicio 1.2
def imprimir_un_verso():
    print("Justo que pensaba en vos, nena, caí muerto \n¿Qué le dio al pequeño dios del centro gris del abismo?\nSólo sé que no soy yo a quien duerme")

# Ejercicio 1.3
def raizDe2():
    return round(math.sqrt(2), 4)

# Ejercicio 1.4
def factorial_de_dos() -> int:
    res:int = 2 * (2-1)
    return res

# Ejercicio 1.5 (*)
def perimetro() -> float:
    res:float = 2*math.pi
    return res

# -

# Ejercicio 2.1
def imprimir_saludo(nombre: str) -> str:
    print("Hola " + nombre)

# Ejercicio 2.2
def raiz_cuadrada_de(numero: int) -> int:
    return math.sqrt(numero)

# Ejercicio 2.3
def fahrenheit_a_celsius(temp_far: float) -> float:
    res: float = ((temp_far - 32)*5) / 9
    return res

# Ejercicio 2.4
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)

# Ejercicio 2.5 (*)
def es_multiplo_de(n:int, m:int) -> bool:
    if ((n%m) == 0):
        return True
    else:
        return False

# Ejercicio 2.6
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero,2)

# Ejercicio 2.7
# def cantidad_de_pizzas(comensales: int, min_cant_de_porciones:int) -> int:

# Ejercicio 3 - Resuelva los siguientes ejercicios utilizando los operadores logicos and, or, not. Resolverlos sin utilizar alternativa condicional (if).

# Ejercicio 3.1
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) or (numero2 == 0)

# Ejercicio 3.2
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return (numero1 == 0) and (numero2 == 0)

# Ejercicio 3.3 (*)
def es_nombre_largo(nombre:str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

# Ejercicio 3.4
def es_bisiesto(año: int) -> bool:
    return (es_multiplo_de(año,400)) or ((es_multiplo_de(año,4)) and not (es_multiplo_de(año,100)))

# Ejercicio 5.1 (*)
def devolver_el_doble_si_es_par(numero:int) -> int:
    if ((numero%2 == 0)):
        return 2*numero
    else:
        return numero

# Ejercicio 6.2 (*)
def imprimir_pares():
    i: int = 10
    while (i<=40):
        if (es_multiplo_de(i, 2)):
            print(i)
        i += 1

# Ejercicio 6.4 (*)
def cuenta_regresiva(n: int):
    while (n>=1):
        print(n)
        n -= 1
    print("Despegue")

# Ejercicio 7.2 (*)
def imprimir_pares2():
    for contador in range(10,41,2):
        print(contador)

# Ejercicio 7.4 (*)
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
# imprimir_un_verso()
# print(raizDe2())
# print(factorial_de_dos())
# imprimir_saludo("Ariana")
# print(raiz_cuadrada_de(25))
# print(fahrenheit_a_celsius(86))
# imprimir_dos_veces("Justo que pensaba en vos, nena, caí muerto\n¿Qué le dio al pequeño dios del centro gris del abismo?\nSólo sé que no soy yo a quien duerme\n")
# print(es_par(10))
# print(es_par(7))
# print(ambos_son_0(1,0))
# print(ambos_son_0(0,1))
# print(ambos_son_0(0,0))
# print(ambos_son_0(1,1))
print(es_bisiesto(1904))
print(es_bisiesto(1900))
print(es_bisiesto(2012))
print(es_bisiesto(2013))