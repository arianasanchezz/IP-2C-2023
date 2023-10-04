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

# EJERCICIO 3 Resuelva los siguientes ejercicios utilizando los operadores logicos and, or, not. Resolverlos sin utilizar alternativa condicional (if).

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

# -

# Ejercicio 4

# -

# EJERCICIO 5 Implementar los siguientes problemas de alternativa condicional (if)

# Ejercicio 5.1 (*)
def devolver_el_doble_si_es_par(numero:int) -> int:
    if (es_multiplo_de(numero,2)):
        return 2*numero
    else:
        return numero

# Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if (es_multiplo_de(numero,2)):
        return numero
    else:
        return (numero + 1)
    
def devolver_valor_si_es_par_sino_el_que_sigue2(numero: int) -> int:
    if (es_multiplo_de(numero,2)):
        return numero
    if not (es_multiplo_de(numero,2)):
        return (numero + 1)
    
# Ejercicio 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if (es_multiplo_de(numero,9)):
        return numero*3
    else:
        if (es_multiplo_de(numero,3)):
            return numero*2
        else:
            return numero
        
# Ejercicio 5.4
def lindo_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

# Ejercicio 5.5
def el_rango(numero: int) -> str:
    if numero < 5:
        print("Menor a 5")
    if numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    if numero > 20:
        print("Mayor a 20")

# Ejercicio 5.6
def trabajo_o_vacaciones(sexo: str, edad: int) -> str:
    if edad < 18 or ((sexo == "F") and (edad >= 60)) or ((sexo == "M") and (edad >= 65)):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

# -

# EJERCICIO 6 Implementar las siguientes funciones usando repeticion condicional while

# Ejercicio 6.1
def imprimir_del_1_al_10():
    i: int = 1
    while (i<11):
        print(i)
        i += 1

# Ejercicio 6.2 (*)
def imprimir_pares():
    i: int = 10
    while (i<=40):
        if (es_multiplo_de(i, 2)):
            print(i)
        i += 1

# Ejercicio 6.3
def eco_eco():
    i: int = 1
    while (i < 11):
        print("eco")
        i += 1

# Ejercicio 6.4 (*)
def cuenta_regresiva(n: int):
    while (n>=1):
        print(n)
        n -= 1
    print("Despegue")

# Ejercicio 6.5
def viaje_en_el_tiempo(año_de_partida: int, año_de_llegada: int):
    while año_de_llegada < año_de_partida:
        print("Viajó un año al pasado, estamos en el año: <" + str(año_de_partida - 1)+">")
        año_de_partida -= 1

# Ejercicio 6.6
def viaje_a_aristoteles(año_de_partida: int):
    while año_de_partida >= (-364):
        print("Viajó 20 años al pasado, estamos en el año: <" + str(año_de_partida - 20)+">")
        año_de_partida -= 20

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
# print(es_bisiesto(1904))
# print(es_bisiesto(1900))
# print(es_bisiesto(2012))
# print(es_bisiesto(2013))
# print(devolver_valor_si_es_par_sino_el_que_sigue(2))
# print(devolver_valor_si_es_par_sino_el_que_sigue(3))
# print(devolver_valor_si_es_par_sino_el_que_sigue2(2))
# print(devolver_valor_si_es_par_sino_el_que_sigue2(3))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(36))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(24))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(20))
# print(lindo_nombre("Ariana"))
# print(lindo_nombre("Ivan"))
# el_rango(4)
# el_rango(17)
# el_rango(25)
# trabajo_o_vacaciones("F",22)
# trabajo_o_vacaciones("M",13)
# trabajo_o_vacaciones("M",60)
# trabajo_o_vacaciones("F",85)
# trabajo_o_vacaciones("M",91)
# imprimir_del_1_al_10()
# eco_eco()
# viaje_en_el_tiempo(2010, 2004)
# viaje_a_aristoteles((-304))