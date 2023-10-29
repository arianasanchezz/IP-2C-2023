# GUIA 7 - EJERCICIO 4 (programas interactivos con input)
# 2. Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE).
#    El usuario debe seleccionar en cada paso si quiere:
#       "C" = Cargar créditos,
#       "D" = Descontar créditos,
#       "X" = Finalizar la simulación (terminar el programa)
#  En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a
#  asumir que el monedero comienza en cero. Para guardar la información grabaremos en el historial tuplas que representen
#  los casos de cargar (“C”, monto a cargar) y descontar crédito (“D”, monto a descontar).

def monedero_electronico():
    monto_total: float = 0
    historial: list[tuple[str, float]] = []
    operacion: str = ""

    while operacion != "X":

        operacion = input("Seleccione el tipo de operación que desea realizar ('C' para cargar, 'D' para descontar, 'X' para finalizar): ")

        if operacion == "C":
            monto = float(input("Ingrese el monto a cargar: "))
            monto_total += monto
            historial.append(("C", monto))
        
        if operacion == "D":
            monto = float(input("Ingrese el monto a descontar: "))
            monto_total -= monto
            historial.append(("D", monto))
    
    return historial

mi_historial = monedero_electronico()
print(mi_historial)